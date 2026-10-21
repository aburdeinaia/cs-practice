def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")

    parts = line.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("В строке должно быть 3 части!")

    time_s, level, message = parts
    valid_levels = {"DEBUG", "INFO", "ERROR", "WARNING"}
    if level not in valid_levels:
        raise ValueError("Несуществующий уровень " + level)

    return {"time": time_s, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts = {}
    
    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1

    return counts


def top_errors(lines, n: int) -> list[list]:
    counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                counts[msg] = counts.get(msg, 0) + 1
        except ValueError:
            continue

    items = [[msg, count] for msg, count in counts.items()]

    def sort_key(pair):
        return (-pair[1], pair[0])

    items.sort(key=sort_key)
    return items[:n]


def format_report(counts: dict, errors: list[list]) -> str:
    report_lines = ["Отчёт по журналу", ""]
    for level in sorted(counts.keys()):
        report_lines.append(level + ": " + str(counts[level]))

    report_lines.append("")
    report_lines.append("Частые ошибки:")

    for msg, count in errors:
        report_lines.append("- " + msg + " — " + str(count))

    return "\n".join(report_lines) + "\n"
