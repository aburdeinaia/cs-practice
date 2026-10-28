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

