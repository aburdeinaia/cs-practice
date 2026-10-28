def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        name = path.split("/")[-1]
        ext = name.split(".")[-1].liwer() if "." in name else ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts

def deepest_path(paths: list[syr]) -> str:
    if not paths:
        return ""
    best_path = path[0]
    best_slashes = best_path.count("/")
    for path in paths:
        current_slashes = path.count("/")
        if  current_slashes > best_slashes or (current_slashes == best_slashes and path < best_path):
            best_path = path
            best_slashes = current_slashes
    return best_path

def human_size(n_bytes: int) -> str:
    # Если размер меньше 1024, выводим байты целым числом
    if n_bytes < 1024:
        bytes_text = str(n_bytes)
        result_string = bytes_text + " Б"
        return result_string
    
    # Для КБ, МБ, ГБ, ТБ делим на 1024 и округляем до 1 знака
    for unit in ["КБ", "МБ", "ГБ", "ТБ"]:
        n_bytes /= 1024
        if n_bytes < 1024 or unit == "ТБ":
            rounded_bytes = round(n_bytes, 1)
            result_string = str(rounded_bytes) + " " + unit
            return result_string
