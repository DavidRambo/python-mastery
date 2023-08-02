"""Ex 2_2"""
import bisect
from collections import Counter, defaultdict
from pprint import pprint

from readrides import read_rides_as_dict

rides = read_rides_as_dict("Data/ctabus.csv")

# 1. How many bus routes exist in Chicago?
# To solve, create a set of the routes.
chi_routes = {row["route"] for row in rides}

print(f"There are {len(chi_routes)} bus routes in Chicago.")  # 181

# 2. How many people rode the number 22 bus on February 2, 2011? What about any
#    route on any date of your choosing?

total_riders_20110202 = sum(
    [
        int(row["rides"])
        for row in rides
        if row["route"] == "22" and row["date"] == "02/02/2011"
    ]
)
# 5055

# 3. What is the total number of rides taken on each bus?
total_rides_per_bus = Counter()
for row in rides:
    total_rides_per_bus[row["route"]] += int(row["rides"])

# pprint(total_rides_per_bus)

# 4. What five bus routes had the greatest ten-year increase in ridership from 2001
#    to 2011?
# ridership_2001 = defaultdict(int)
# ridership_2011 = defaultdict(int)
ridership = defaultdict(int)
ten_year_incr: list[dict] = []

for row in rides:
    if "2001" in row["date"]:
        ridership[row["route"]] += int(row["rides"])
    if "2011" in row["date"]:
        ridership[row["route"]] -= int(row["rides"])


ten_year_incr = sorted(((v, k) for k, v in ridership.items()), reverse=True)

pprint(ten_year_incr[:5])
