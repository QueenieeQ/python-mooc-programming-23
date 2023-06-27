
# Write your solution here
list = [1,2,3,4,5]
index = 0
# index = input("Index:")
while index >= 0 and index < len(list):
    index = int(input("Index:"))
    if index ==(-1):
        break
    values =  int(input("New value: "))
    list[index] = values
    print(list)