# Write your solution here
my_list = []
while True:
    item = int(input("new items:"))
    if item == 0:
        print("Bye!")
        break
    my_list.append(item)
    print(f"The list now: {my_list}")
    print(f"The list in order: {sorted(my_list)}")
        