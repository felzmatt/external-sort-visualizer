import sys
from algorithm.sort_algorithm import Sort

def main():
    if '--sort' in sys.argv:
        B, F = map(int, input('B, F = ').replace(',',' ').split())
        sort = Sort(B, F)
        sort.sort()

        for step in sort.steps:
            print(step)
        history = sort.export_json()
        print(f"Exported in JSON: {history}")

        if "--export-history" in sys.argv:
            with open("history.json", "w") as f:
                f.write(history)
if __name__ == "__main__":
    main()
