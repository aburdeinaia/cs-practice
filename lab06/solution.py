def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        name = path.split("/")[-1]
        ext = name.split(".")[-1].liwer() if "." in name else ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts
