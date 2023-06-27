# Write your solution here
# You can test your function by calling it within the following block
def range_of_list( list1):
    return max(list1)-min(list1)
if __name__ == "__main__":
    my_list = [1, 2, 3]
    result = range_of_list(my_list)
    print(f"The range of the list is {result}")
    for item in my_list:
        print(item)
        