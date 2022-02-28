def fits_in(pair, num):
    if (num >= pair[0]) and (num < pair[1]): #строго меньше даты выезда
        return True
    else:
        return False


def max_guests(pairs):
    if not pairs:
        return 0
    starts = []
    ends = []
    for a, b in pairs:
        starts.append(a)
        ends.append(b)
    start = min(starts)
    end = max(ends)
    # print("start:", start, "; end:", end)
    total = list(range(start, end))
    counts = [0 for i in range(start, end + 1)]
    for i in total: #подсчет яисла гостей
        for pair in pairs:
            if fits_in(pair, i):
                counts[i] += 1
    return max(counts)


if __name__ == '__main__':
    #test = []
    #test = [(1, 2)]
    #test = [(1, 2), (2, 3)]
    test = [(1, 5), (0, 1), (4, 5)]

    result = max_guests(test)
    print("Максимальное число гостей единомоментно:", result)
