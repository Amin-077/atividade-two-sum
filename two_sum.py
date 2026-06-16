def two_sum(nums, target):
    mapa = {}

    for i, num in enumerate(nums):
        complemento = target - num

        if complemento in mapa:
            return [mapa[complemento], i]

        mapa[num] = i

    return []


# Testes
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))