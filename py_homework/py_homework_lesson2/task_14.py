print(" v--- Честно говоря я в интеренете почитал, как правильно транспонировать")
array = [
    [11,12,13,14,15],
    [21,22,23,24,25],
    [31,32,33,34,35],
    [41,42,43,44,45],
    [51,52,53,54,55],
]
transposed = [list(row) for row in zip(*array)]
for row in transposed:
    print(str(row))
