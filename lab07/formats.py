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
