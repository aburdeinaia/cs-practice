
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

