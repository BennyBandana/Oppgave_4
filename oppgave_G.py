
from typing import List, Tuple

def beregn_trend(x: List[float], y: List[float]) -> Tuple[float, float]:
    # Antall datapunkter
    n = len(x)
    
    # Beregne gjennomsnitt av x og y
    avg_x = sum(x) / n
    avg_y = sum(y) / n
    
    # Beregne a og b basert på gitte formler
    a = sum((xi - avg_x) * (yi - avg_y) for xi, yi in zip(x, y)) / sum((xi - avg_x) ** 2 for xi in x)
    b = avg_y - a * avg_x
    
    return a, b