u = [False, True]
for x in u:
    for y in u:
        for z in u:
            for w in u:
                if not (not w or (x or not z) and (not x or not y or z) and not w or (x or not z) and (not x or not y or z)):
                    print(int(x), int(y), int(z), int(w))