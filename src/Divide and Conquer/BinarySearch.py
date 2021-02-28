def binary_search(array, key):
    bottom, top = 0, len(array) - 1

    while top >= bottom:
        guess = int((top + bottom) / 2)

        if array[guess] == key:
            return guess
        elif array[guess] > key:
            top = guess - 1
        else:
            bottom = guess + 1

    return None

def rec_binary_search(array, key, bottom, top):
    if top < bottom:
        return None

    guess = int((top + bottom) / 2)

    if array[guess] == key:
        return guess
    elif array[guess] > key:
        return rec_binary_search(array, key, bottom, guess-1)
    else:
        return rec_binary_search(array, key, guess+1, top)

array = [1, 1, 2, 4, 5, 7, 11, 21, 34, 76, 99]
print(binary_search(array, 21))
print(rec_binary_search(array, 21, 0, len(array)-1))