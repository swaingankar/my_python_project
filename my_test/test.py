from collections import OrderedDict

a = [(5, 3), (3, 1), (3, 2), (5, 0), (6, 4)]
d = OrderedDict()

for item in a:

    # Get old value in dictionary if exist
    old = d.get(item[0])

    # Skip if new item is larger than old
    if old:
        if item[1] > old[1]:
            continue
        #else:
        #    del d[item[0]]

    # Assign
    d[item[0]] = item

print(list(d.values()))
