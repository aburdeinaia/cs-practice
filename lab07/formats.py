import json

def csv_to_records(text):
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
            col_val = values[i].strip()
            record[col_name] = col_val
        records.append(record)
    return records

def to_type(value):
    text = value.strip()
    low = text.lower()
    if low == "true" or low == "yes":
        return True
    if low == "false" or low == "no":
        return False

    try:
        return int(text)
    except ValueError:
        pass

    try:
        return float(text)
    except ValueError:
        pass
    return text

def merge_by_key(rows, extra, key):
    result = []
    for row in rows:
        new_row = {}
        key_value = row.get(key)
        if key_value in extra:
            info = extra[key_value]
            for k in info:
                new_row[k] = info[k]
        for k in row:
            new_row[k] = row[k]
        result.append(new_row)
    return result


def records_to_json(records):
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
