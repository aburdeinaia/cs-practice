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
    counts = { "BROKEN": 0, "DEBUG": 0, "ERROR": 0, "INFO": 0, "WARNING": 0  }
    
    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] += 1
        except ValueError:
            counts["BROKEN"] += 1

    return counts
