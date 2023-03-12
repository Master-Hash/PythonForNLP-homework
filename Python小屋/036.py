def main(*para: int) -> float:
    return round(1 / sum(map(lambda x: 1 / x, para)), 1)
