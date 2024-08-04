def reverse_list(arr):
    reversed_list = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_list.append(arr[i])
    return reversed_list

my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
print("Reversed list:", reverse_list(my_list))
