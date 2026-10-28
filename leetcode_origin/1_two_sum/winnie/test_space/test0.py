# figure out the hashmap

def twoSum(ls, tar):
    hashmap = {}
    for i in range(len(ls)):
        hashmap[ls[i]] = i

    return hashmap


list1 = [2, 5, 3, 1, 6, 5]
target = 8
print(twoSum(list1, target))
