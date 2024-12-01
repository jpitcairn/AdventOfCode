import argparse
import importlib

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", type=int, choices=range(2024, 2024), default=2024)
    parser.add_argument("-d", "--day", type=int, choices=range(1, 26))
    parser.add_argument("-p", "--part", type=int, choices=range(1, 3))
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    # Import the module based on the year and day
    module_name = f"adventofcode.puzzles.{args.year}.{args.day:02}"
    module = importlib.import_module(module_name)
    # Call the solve function from the module
    result = module.solve()
    print(f"Part 1 Answer: {result[0]}")
    print(f"Part 2 Answer: {result[1]}")

if __name__ == "__main__":
    main()
