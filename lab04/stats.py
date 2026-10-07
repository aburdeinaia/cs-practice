def parse_record(line: str) -> tuple[str, float, str]:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")

    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Неверное количество полей: ожидается 3, найдено {len(parts)}")

    city, temp_str, date = parts

    if not city.strip():
        raise ValueError("Город не может быть пустым")
    if not date.strip():
        raise ValueError("Дата не может быть пустой")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура не является числом: '{temp_str}'")

    return city.strip(), temp, date.strip()


