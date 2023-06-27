# Write your solution here
interger = int(input("Please type in a positive interger:"))
list1 = list(range(interger))
print(list1)
list1.remove(0)
for i in range((-interger), interger, 1):
    if i != 0:
        print(i)
    # if i == 0:
