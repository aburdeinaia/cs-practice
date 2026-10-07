import sys
from stats import average_by_city, read_valid, warmest_city

def main():
    lines = sys.stdin.read().splitlines()

    valid_records, error_count = read_valid(lines)
    valid_count = len(valid_records)

    averages = average_by_city(valid_records)
    warmest = warmest_city(averages)

    print(valid_count)
    print(error_count)

    if warmest is not None:
        print(f"{averages[warmest]:.1f}")
    else:
        print("0.0")

if __name__ == "__main__":
    main()
