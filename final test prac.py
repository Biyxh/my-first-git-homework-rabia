from test import num_arr


def twoSumHashing(num_arr, pair_sum):
    sums = []
    hash_table = {}

    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hash_table:
            print("Pair with sum", pair_sum, "is: (", num_arr[i], ",", complement, ")")
        hash_table[num_arr[i]] = num_arr[i]


lst = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())

    lst.append(ele)

print(lst)

pair_sum = 9

twoSumHashing(num_arr, pair_sum)
