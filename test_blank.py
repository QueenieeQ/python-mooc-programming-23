my_list = [1,2,3,4,6,1,6,9]

# new_list = list.sorted()

my_list.sort()
print(my_list)
print(sorted(my_list))

greatest = max(my_list)
smallest = min(my_list)
sum = sum(my_list)
print(greatest)
print(smallest)
print(sum)



def median(my_list: list):
    ordered = sorted(my_list)
    list_centre = len(ordered) //2
    return ordered[list_centre]
number = [5,3,2,1,5]
print(number)
print("the median of list:", median(number))