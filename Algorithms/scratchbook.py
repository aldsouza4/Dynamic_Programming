arr = [1, 3, 5, 7, 9, 11]

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        print(i)

    else:
        print("none")

# Output
# none
# none
# none
# none
# none
