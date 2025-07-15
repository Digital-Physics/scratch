def closedTimelikeCurve(x):
    if bin(x) == '0b11110100': # fixed point
        print(x)
        return closedTimelikeCurve(x)
    else:
        return closedTimelikeCurve(x + 1)

print(closedTimelikeCurve(0))