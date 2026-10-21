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
