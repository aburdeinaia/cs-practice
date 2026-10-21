import sys
from logstats import count_levels, top_errors, format_report

def main():
    file_name = sys.stdin.readline().strip()
    if not filename:
        return

    with open(file_name, "r", encoding="utf-8") as log_file:
        counts = count_levels(log_file)

    total_parsed = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    print(total_parsed)
    print(error_count)
    print(broken_count)

    with open(file_name, "r", encoding="utf-8") as log_file:
        errors = top_errors(log_file, n=3)

    report_text = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_text)

if __name__ == "__main__":
    main()
