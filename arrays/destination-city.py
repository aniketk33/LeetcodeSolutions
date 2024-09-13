def destination_city(paths):
    source_city = set()

    # adding all the source cities to a set. why? as a result is guaranteed, the only destination will be left out
    for source, _ in paths:
        source_city.add(source)

    # if destination not found in the source cities, then it is the final destination
    for _, curr_destination in paths:
        if curr_destination not in source_city:
            return curr_destination


def destination_city_2(paths):
    source, dest = set(), set()

    for s, d in paths:
        source.add(s)
        dest.add(d)

    # return the unique value from destination set
    return (dest - source).pop()


# res = destination_city([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
res = destination_city_2([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
print(res)
