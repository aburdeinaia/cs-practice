
def parse_record(line: str) -> dict:
    
    fields = line.split(";")
    if len(fields) != 3:
        raise ValueError("Строка должна содержать ровно три поля, разделенных ';'")
    
    city, temperature_str, date = fields

    city = fields[0].strip()
    temperature_str = fields[1].strip()
    date = fields[2].strip()
    
    temperature_str = temperature_str.replace(",", ".")

    if not city.strip() or not date.strip():
        raise ValueError("Название города и дата не могут быть пустыми")
        
    try:
        temperature = float(temperature_str)
    except ValueError:
        raise ValueError(f"Некорректный формат температуры: '{temperature_str}'")
        
    return {"city": city, "temperature": temperature, "date": date}

def read_valid(lines: list[str]) -> list[dict]:

    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for r in records:
        city = r["city"]
        totals[city] = totals.get(city, 0.0) + r["temperature"]
        counts[city] = counts.get(city, 0) + 1
        
    averages = {}
    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)
    return averages

def warmest_city(records: list[dict]) -> str:

    if not records:
        return ""
        
    averages = average_by_city(records)
    
    best_city = None
    max_temperature = float('-inf')
    
    for city, avg_temperature in averages.items():
        if avg_temperature > max_temperature:
            max_temperature = avg_temperature
            best_city = city
        elif avg_temperature == max_temperature:
            
            if best_city is None or city < best_city:
                best_city = city
                
    return best_city
