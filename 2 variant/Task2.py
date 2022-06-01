u = [False, True] #
i = [False, True]
o = [False, True]
p = [False, True]
for x in u:
    for y in i:
        for z in o:
            for w in p:
                if not (not w or (x or not z) and (not x or not y or z) and not w or (x or not z) and (not x or not y or z)):
                    print(int(x), int(y), int(z), int(w))