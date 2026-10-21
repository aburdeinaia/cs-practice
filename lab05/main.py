import sys
from logstats import count_levels, top_errors, format_report

def main():
    filename = sys.stdin.readline().strip()
    if not filename:
        return

    with open(filename, encoding="utf-8") as log:
        counts = count_levels(log)

    total_lines = sum(counts.values())
    broken_count = counts.get("BROKEN", 0)
    error_count = counts.get("ERROR", 0)
    

    print(total_lines)
    print(broken_count)
    print(error_count)

    with open(filename, encoding="utf-8") as log:
        errors = top_errors(log, n=10)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(format_report(counts, errors))

if __name__ == "__main__":
    main()
