def IOC(in_str):
    l = list(0 for i in range(26))
    for i in in_str:
        l[ord(i)-65] += 1
    length = len(in_str)
    tot = 0.0
    for i in l:
        tot += (i*(i-1))
    return tot/(length*(length-1))
