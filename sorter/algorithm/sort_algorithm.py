import math
from algorithm.data import Tuple, Frame, AlgorithmStep, AlgorithmPhase
from copy import deepcopy
import datetime
import json

class Sort:
    """
    This class simulates the algorithm by representing the used data structure and recording each step.
    """
    def __init__(self, F: int, P: int, csvdata):
        self.F = F
        self.P = P
        self.B = math.ceil(len(csvdata)/P)
        self.tuples_per_frame = P

        self.steps = []
        self.buffer = []
        self.relation = []
        self.init_time = datetime.datetime.now()
        self.execution_time = 0

        for _ in range(self.F):
            data = [Tuple(empty = True) for _ in range(self.tuples_per_frame)]
            self.buffer.append(Frame(data))

        for i in range(self.B):
            data = []
            for j in range(self.tuples_per_frame):
                if i*self.tuples_per_frame + j < len(csvdata):
                    data.append(Tuple(value=csvdata[i*self.tuples_per_frame + j]))
                else:
                    data.append(Tuple(empty= True))
            self.relation.append(Frame(data))
    
    def export_json(self):
        index = 0
        number_of_steps = len(self.steps)
        history = {
            "init_time": self.init_time.strftime('%H:%M:%S'),
            "execution_time": str(self.execution_time),
            "tuples": self.B*self.tuples_per_frame,
            "pages": self.B,
            "frames": self.F,
            "number_of_steps": number_of_steps,
            "steps" : []
        }
        for step in self.steps:
            history["steps"].append(step.create_json_step(index))
            index += 1
        
        return json.dumps(history, indent=4)
        

    """
    Execute the sorting and append transitions to the tape
    """
    def sort(self):
        self.snapshot('Step 1: Create runs')

        run_start, run_end = [], []
        for i in range(0, self.B, self.F):
            run_length = min(self.F, self.B - i)

            run_start.append(i)
            run_end.append(i + run_length)

            for j in range(run_length):
                self.buffer[j], self.relation[i+j] = self.relation[i+j], self.buffer[j]

            self.snapshot(f'Load {run_length} frames')
            self.sort_buffer(0, run_length)
            self.snapshot('Sort frames')

            for j in range(run_length):
                self.buffer[j], self.relation[i+j] = self.relation[i+j], self.buffer[j]

            self.snapshot(f'Store sorted run {i // self.F}')

        # Step 2...N. Merge runs together

        self.snapshot('Step 2: Merge runs')

        if self.F == 2 and len(run_start) > 1:
            self.snapshot('Cannot merge with only 2 frames')
            return

        while len(run_start) > 1:

            new_run_start, new_run_end = [], []

            for first_frame in range(0, len(run_start), self.F - 1):
                num_runs = min(self.F - 1, len(run_start) - first_frame)
                output_frames = []
                output_start = run_start[first_frame]

                new_run_start.append(run_start[first_frame])
                new_run_end.append(run_end[first_frame + num_runs - 1])

                # Load the first frame of each run
                for j in range(num_runs):
                    self.load_frame(run_start[first_frame + j], j)

                # Prepare output frame
                self.buffer[num_runs].clear()

                self.snapshot(f'Load first frames for {run_start[first_frame]} - {run_end[first_frame+num_runs-1]}. Runs length = {num_runs}')

                while True:
                    frame_id, t = self.next_min_tuple(0, num_runs)

                    # Merge completed
                    if t is None:
                        break

                    # Add tuple to output frame
                    self.buffer[self.F - 1].insert_tuple(t)

                    self.snapshot(f'Output min element {t}', frame_id)

                    # Flush if needed
                    if self.buffer[self.F - 1].num_tuples() == self.tuples_per_frame:
                        output_frames.append(deepcopy(self.buffer[self.F - 1]))
                        self.buffer[self.F - 1].clear()

                        self.snapshot('Flush output frame')

                    # Load new input frame
                    if self.buffer[frame_id].num_tuples() == 0:
                        run_start[first_frame + frame_id] += 1
                        if run_start[first_frame + frame_id] < run_end[first_frame + frame_id]:
                            self.load_frame(run_start[first_frame + frame_id], frame_id)

                            self.snapshot('Load new input frame')

                # F-1 runs are sorted into one
                self.relation[output_start:output_start + len(output_frames)] = output_frames

            run_start, run_end = new_run_start, new_run_end

        self.snapshot('Done')
        self.execution_time = datetime.datetime.now() - self.init_time


    def sort_buffer(self, start, end):
        items = []
        for i in range(start, end):
            items += self.buffer[i].data

        items.sort()

        for i in range(start, end):
            self.buffer[i].data = items[i * self.tuples_per_frame : (i+1) * self.tuples_per_frame]

    def next_min_tuple(self, start, end):
        idx, cur_best = -1, None
        for i,frame in enumerate(self.buffer[start:end]):
            t = frame.get_first_tuple()
            if t is None:
                continue

            if cur_best is None or t < cur_best:
                cur_best = t
                idx = i

        if idx == -1: return idx, None

        return idx, self.buffer[idx].pop_first_tuple()

    def load_frame(self, pos_in_relation, pos_in_buffer):
        self.buffer[pos_in_buffer], self.relation[pos_in_relation] = \
            self.relation[pos_in_relation], self.buffer[pos_in_buffer]

    def snapshot(self, phase: AlgorithmPhase, min_index: int = -1):
        self.steps.append(AlgorithmStep(self.buffer, self.relation, phase, min_index))
