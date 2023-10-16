from functools import total_ordering
from copy import copy, deepcopy
from typing import List
import enum

@total_ordering
class Tuple:
    """
    Total ordering is defined over this class. The ordering is performed over all attributes.
    Empty is used to track empty space if frames of both pages and buffer.
    """
    def __init__(self, value = 0, empty = False):
        self.value = value
        self.empty = empty
    
    def __str__(self):
        return "-" if self.empty else str(self.value)

    def __lt__(self, other):
        return self.value < other.value
    def __eq__(self, other):
        return self.value == other.value
    def __repr__(self):
        return '-' if self.empty else str(self.value)

class Frame:
    """
    Fixed size frame
    """
    def __init__(self, data: List[Tuple]):
        self.data = data

    def clear(self):
        for t in self.data:
            t.empty = True

    def num_tuples(self):
        ctr = 0
        for t in self.data:
            if not t.empty:
                ctr += 1
        return ctr

    def get_first_tuple(self):
        for t in self.data:
            if not t.empty:
                return t
        return None

    def pop_first_tuple(self):
        for t in self.data:
            if not t.empty:
                res = deepcopy(t)
                t.empty = True
                return res
        return None

    def insert_tuple(self, x):
        for i,t in enumerate(self.data):
            if t.empty:
                self.data[i] = deepcopy(x)
                break

    def __repr__(self):
        return str(self.data)
    def __len__(self):
        return len(self.data)

class AlgorithmPhase(enum.Enum):
    CREATE_RUNS = 0,
    MERGE_RUNS = 1

class AlgorithmStep:
    """
    A snapshot of the relation and buffer state
    """
    def __init__(self, buffer: List[Frame], relation: List[Frame], phase: AlgorithmPhase, min_index: int):
        self.buffer = [deepcopy(f) for f in buffer]
        self.relation = [deepcopy(f) for f in relation]
        self.min_index = min_index
        self.phase = phase
        

    def __repr__(self):
        return f'relation={self.relation}\n' \
            + f'buffer={self.buffer}\n' \
            + (f' ({self.min_index})') \
            + '\n'
    
    def create_json_step(self, index):
        json_step = {
            "index": index,
            "phase": self.phase,
            "relation": [[tup.value if not tup.empty else None for tup in page.data] for page in self.relation],
            "buffer": [[tup.value if not tup.empty else None for tup in frame.data] for frame in self.buffer],
            "min_index": self.min_index,
        }
        return json_step
