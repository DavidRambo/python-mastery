"""Ex2_1: Compare the memory usage of various data structures."""

import collections
import csv
import sys
import tracemalloc
import typing

filepath = "Data/ctabus.csv"


def read_rides_as_tuples(filename):
    """Read the bus ride data as a list of tuples."""
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = row[3]
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dict(filename):
    """Read the bus ride data as a list of dictionaries."""
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # skip headers
        for row in rows:
            record = {}  # Must create here to break reference to previous dict.
            record["route"] = row[0]
            record["date"] = row[1]
            record["daytype"] = row[2]
            record["rides"] = row[3]
            records.append(record)
    return records


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


class SlottedRow:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


class RowNT(typing.NamedTuple):
    route: str
    date: str
    daytype: str
    rides: str


def read_rides_as_class(filename):
    """Read the bus ride data as a list of classes."""
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # skip headers
        for row in rows:
            record = Row(row[0], row[1], row[2], row[3])
            records.append(record)
    return records


def read_rides_with_slots(filename):
    """Read the bus ride data as a list of slotted classes."""
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # skip headers
        for row in rows:
            record = SlottedRow(row[0], row[1], row[2], row[3])
            records.append(record)
    return records


def read_rides_as_named_tuple(filename):
    """Read the bus ride data as a list of named tuples created as classes."""
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # skip headers
        for row in rows:
            record = RowNT(row[0], row[1], row[2], row[3])
            records.append(record)
    return records


def read_rides_as_named_tuple2(filename):
    """Read the bus ride data as a list of named tuples created via collections."""
    records = []
    RowNT = collections.namedtuple("Stock", ["route", "date", "daytype", "rides"])
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # skip headers
        for row in rows:
            record = RowNT(row[0], row[1], row[2], row[3])
            records.append(record)
    return records


def test_memory(choice: str) -> tuple[int, int]:
    """Driver function testing the memory usage of above alternatives."""
    tracemalloc.start()
    r: list
    if choice == "tuple":
        r = read_rides_as_tuples(filepath)
    elif choice == "dict":
        r = read_rides_as_dict(filepath)
    elif choice == "class":
        r = read_rides_as_class(filepath)
    elif choice == "slot":
        r = read_rides_with_slots(filepath)
    elif choice == "named":
        r = read_rides_as_named_tuple(filepath)
    elif choice == "named2":
        r = read_rides_as_named_tuple2(filepath)
    else:
        print("Invalid function selection.")

    return tracemalloc.get_traced_memory()


# Ex 2_5
def read_rides_as_columns(filename):
    """Read the bus ride data into 4 lists, representing columns."""
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(row[3])
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)


class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [
                {
                    "route": self.routes[idx],
                    "date": self.dates[idx],
                    "daytype": self.daytypes[idx],
                    "rides": self.numrides[idx],
                }
                for idx in range(
                    index.start, index.stop, index.step if index.step is not None else 1
                )
            ]
        return {
            "route": self.routes[index],
            "date": self.dates[index],
            "daytype": self.daytypes[index],
            "rides": self.numrides[index],
        }

    def append(self, d):
        self.routes.append(d["route"])
        self.dates.append(d["date"])
        self.daytypes.append(d["daytype"])
        self.numrides.append(d["rides"])


def read_rides_as_dict2(filename):
    """Read the bus ride data as a list of dictionaries."""
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # skip headers
        for row in rows:
            record = {}  # Must create here to break reference to previous dict.
            record["route"] = row[0]
            record["date"] = row[1]
            record["daytype"] = row[2]
            record["rides"] = row[3]
            records.append(record)
    return records


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect usage. Provide as an argument one of the following:")
        print("> tuple")
        print("> dict")
        print("> class")
        print("> slot")
        print("> named")
        print("> named2")
    current, peak = test_memory(sys.argv[1])
    print(f"{current=}\n{peak=}")
