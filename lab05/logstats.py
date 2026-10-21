def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")

    parts = line.split(maxsplit = 2)
    if len(parts) < 3:
        raise ValueError("В строке должно быть 3 части!")

    time_s, level, message = parts
    valid_levels = {"DEBUG", "INFO", "ERROR", "WARNING"}
    if level not in valid_levels:
        raise ValueError("Несуществующий уровень " + level)
    return{"time": time_s, "level": level, "message": message}

def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        line = line.strip()
        if not line:
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
        line = line.strip()
        if not line:
            continue

        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                if msg in counts:
                    counts[msg] += 1
                else:
                    counts[msg] = 1
        except ValueError:
            continue
        
items = []
for msg, count in counts.items():
    items.append([msg, count])
    
    def sort_key(pair):
        # pair — это [сообщение, количество]
        return (-pair[1], pair[0])

    items.sort(key=sort_key)
        #Топ-n самых частых ошибок
    return items[:n]


def format_report(counts: dict, errors: list[list]) -> str:
    levels_order = sorted(counts.keys())  # алфавитный порядок уровней

    report_lines = ["Отчёт по журналу", ""]

    for level in levels_order:
        report_lines.append(f"{level}: {counts[level]}")

    report_lines.append("")
    report_lines.append("Самые частые ошибки:")

    if errors:
        for msg, count in errors:
            report_lines.append(f"- {msg} — {count}")

    report = "\n".join(report_lines) + "\n"
    return report
