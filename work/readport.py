"""Ex 2_2 part A"""

import csv


def read_portfolio(filename: str) -> list[dict]:
    """Reads a csv file and returns as a list of dicts."""
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)
        for row in rows:
            record = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(record)
    return portfolio
