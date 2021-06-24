def IOC(in_str):
    # Formula for IOC: <https://en.wikipedia.org/wiki/Index_of_coincidence>
    # c * ((n_a/N * (n_a - 1)/(N - 1)) + (n_b/N * (n_b - 1)/(N - 1)) + ... + (n_z/N * (n_z - 1)/(N - 1))
    # Or as a summation:
    # Sigma n_i(n_i - 1)/((N(N - 1))/c)
    # Where:
    # c is the normalising coefficient, 26 for English
    # n_{letter} is the count of that letter
    # n_i is the count for any letter
    # N is the length of the text
    # Taken from William Banks, Github <https://github.com/Will-Banksy>
    l = list(0 for i in range(26))
    for i in in_str:
        l[ord(i)-65] += 1
    length = len(in_str)
    tot = 0.0
    for i in l:
        tot += (i*(i-1))
    return tot/(length*(length-1))
