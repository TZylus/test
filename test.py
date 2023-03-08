import random

# create empty array and length
n = 10
arr = []

# appends random values into arr with range 1-100
for i in range (n):
    arr.append(random.randint(1,100))
print(arr)

# create a new array to avoid any duplicates in the list
non_Dupe = []

for i in arr:
    # 'not in' operator tests whether value being appended is already inside the new array 'non_dupe'
    if i not in non_Dupe:
        non_Dupe.append(i)

# bubble sort method to arrange the new array in descending order
def sort(non_Dupe):
    for i in range(len(non_Dupe)):
        # for loop to compare all array elements (bubbleSort)
        for j in range (0, len(non_Dupe) - i - 1):
            if non_Dupe[j] < non_Dupe [j +1]:
                # create a temp array to rearrange and store temporary variables that needs swapping
                tempArray = non_Dupe[j]
                non_Dupe[j] = non_Dupe[j+1]
                non_Dupe[j+1] = tempArray

# call function and print results
sort(non_Dupe)
print(non_Dupe)
