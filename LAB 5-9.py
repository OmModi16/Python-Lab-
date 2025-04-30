list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 5, 6, 8, 9]
list3 = [num for num in list1 if num not in list2]
print("First list:", list1)
print("Second list:", list2)
print("Third list (numbers in first list not in second list):", list3)
