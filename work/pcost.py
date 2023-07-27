# pcost.py (ex 1_3)
# from pathlib import Path
#
# total = 0.0
#
# portfolio = Path(Path.home() / "repos" / "python-mastery" / "Data" / "portfolio.dat")
#
# with open(portfolio, "rb") as f:
#     for line in f:
#         parted_line = line.split()
#         total += int(parted_line[1]) * float(parted_line[2])
#
# print(f"Total cost: {total}")

# pcost.py (ex 1_4)


def portfolio_cost(filename: str) -> float:
    total = 0.0

    with open(filename, "rb") as f:
        for line in f:
            parted_line = line.split()
            try:
                shares = int(parted_line[1])
                price = float(parted_line[2])
                total += shares * price
            except ValueError as val_err:
                print(f"Couldn't parse {line}")
                print(f"Reason: {val_err}")

    return total


if __name__ == "__main__":
    print(">>> Running portfolio_cost() on Data/portfolio.dat")
    print(portfolio_cost("Data/portfolio.dat"))
    print("\n")
    print(">>> Running portfolio_cost() on Data/portfolio3.dat")
    print(portfolio_cost("Data/portfolio3.dat"))
