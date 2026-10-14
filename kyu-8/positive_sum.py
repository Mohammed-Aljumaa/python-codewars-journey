def positive_sum(arr):
    total = 0

    for number in arr:
        if number > 0:
            total += number

    return total
