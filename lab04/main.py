import sys
from stats import average_by_city, read_valid, warmest_city, parse_record

def main():
    lines = sys.stdin.read().splitlines()
    
    valid_count = 0
    error_count = 0
    valid_records = []
    
    for line in lines:
        if not line.strip():
            continue  
        try:
            record = parse_record(line)
            valid_records.append(record)
            valid_count += 1
        except ValueError:
            error_count += 1  
    print(valid_count)

    print(error_count)   

    if valid_records:
        best_city = warmest_city(valid_records)
        averages = average_by_city(valid_records)
        print(f"{averages[best_city]:.1f}")
    else:
        print("0.0")

if __name__ == "__main__":
    main()
