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

   return {
        "city": city.strip(),
        "temp": temp,
        "date": date.strip()
    } 
def read_valid(lines: list[str]) -> tuple[list[tuple[str, float, str]], int]:
    valid_records = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue

    return valid_records
def average_by_city(records:list[dict]) -> dict:

    total = {}
    count = {}

    for rec in records:
        city = rec["city"]
        temp = rec["temp"]

        total[city] = total.get(city, 0.0) + temp
        count[city] = count.get(city, 0) + 1

    averages = {}
    for city in total:
        avg = total[city] / count[city]
        averages[city] = round(avg, 1)

    return averages 

def warmest_city(averages: dict[str, float]) -> str | None:
    if not averages:
        return None

    best_city = None
    best_avg = None

    for city, avg in averages.items():
        if best_avg is None or avg > best_avg:
            best_avg = avg
            best_city = city

    return best_city
