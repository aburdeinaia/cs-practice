import numpy as np

def make_hours() -> list[int]:
    arr = np.arange(0, 22, 3, dtype=int)
    return arr.tolist()

def vector_report(values: list[float]) -> dict:
    arr = np.asarray(values, dtype=float)
    
    third_elem = arr[2].item()
    last_elem = arr[-1].item()
    middle_slice = arr[2:6].tolist()
    every_second_slice = arr[::2].tolist()
    reversed_arr = arr[::-1].tolist()
    
    return {
        "third": third_elem,
        "last": last_elem,
        "middle": middle_slice,
        "every_second": every_second_slice,
        "reversed": reversed_arr,
    }

def change_vector(values: list[float]) -> list[float]:
    arr = np.asarray(values, dtype=float).copy()
    arr[2:5] = 99
    arr[::2] = -1
    return arr.tolist()

def cap_above(values: list[float], limit: float) -> list[float]:
    arr = np.asarray(values, dtype=float).copy()
    arr[arr > limit] = limit
    return arr.tolist()

def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    arr = np.asarray(values, dtype=float)
    fahrenheit = arr * 9 / 5 + 32
    return fahrenheit.tolist()
