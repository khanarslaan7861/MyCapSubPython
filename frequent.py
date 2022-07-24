def most_frequent(il):
    di = {}
    for i in il:
        di[f'{i}'] = di.get(f'{i}', 0) + 1
    sortd = sorted(di.items(), key=lambda x: x[1], reverse=True)
    return sortd


st = input("Please enter a string: ").lower()
freq = most_frequent(st)
for j in freq:
    print(f'{j[0]} = {j[1]}')
