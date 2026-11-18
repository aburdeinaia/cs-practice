import json

def csv_to_records(text:str) -> list[dict]:
    lines = text.splitlines()
    clean_lines = []
    for line in lines:
        if line.strip() != "":
            clean_lines.append(line)
    if len(clean_lines) == 0:
        return []
    headers = clean_lines[0].split(",")
    records = []
    for line in clean_lines[1:]:
        values = line.split(",")
        record = {}
        for i in range(len(headers)):
            col_name = headers[i].strip()
            col_val = values[i].strip() if i < len(values) else ""
            record[col_name] = col_val
        records.append(record)
    return records

def to_type(text: str):
    low = text.lower()
    if low == "true" or low == "yes":
        return True
    if low == "false" or low == "no":
        return False

    if "_" not in text:
        try:
            return int(text)
        except ValueError:
            pass

        float_text = text.replace(",",".") if text.count(",") ==1 else text
        if float_text.lower() not in ("nan", "inf", "+inf", "-inf", "infinity", "+infinity", "-infinity"):
            try:
                return float(float_text)
            except ValueError:
                pass

    return text

def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list = None

    for raw_line in lines:
        #Убираем все после символа "#" и пробелы по краям
        line = raw_line.split("#", 1)[0].strip()

        if line == "":
            continue

        is_list_item = line.startswith("- ") or line == "-"
        if current_list is not None and is_list_item:
            item_text = line[1:].strip()
            result[current_list].append(to_type(item_text))
        elif ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()

            if val == "":
                result[key] = []
                current_list = key
            else:
                result[key] = to_type(val)
                current_list = None
        else:
            current_list = None

    return result
def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []
    for row in rows:
        new_row = {}
        key_value = row.get(key)
        if key_value is not None and key_value in extra:
            info = extra[key_value]
            for k in info:
                new_row[k] = info[k]
        for k in row:
            new_row[k] = row[k]
        result.append(new_row)
    return result


def records_to_json(records):
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
