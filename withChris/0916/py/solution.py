def ArrayChallenge_O_lgN(arr):
    if len(arr) >= 3:
        mid_idx = len(arr) // 2
        if (arr[mid_idx + 1] - arr[mid_idx]) * (arr[mid_idx] - arr[mid_idx - 1]) < 0:
            return mid_idx
        else:
            ArrayChallenge_O_lgN(arr[0:mid_idx])
            ArrayChallenge_O_lgN(arr[mid_idx:len(arr)])

    return -1


print(ArrayChallenge_O_lgN([-4, -2, 9, 10]))
print(ArrayChallenge_O_lgN([5, 4, 3, 2, 10, 11]))