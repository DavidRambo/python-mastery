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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect usage. Provie as an argument one of the following:")
        print("> tuple")
        print("> dict")
        print("> class")
        print("> slot")
        print("> named")
        print("> named2")
    current, peak = test_memory(sys.argv[1])
    print(f"{current=}\n{peak=}")
