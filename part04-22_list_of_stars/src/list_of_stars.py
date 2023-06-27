# Write your solution here
def list_of_stars(my_list: list):
    for number in my_list:
        print("*" * number)
    # return print(list2)
if __name__ == "__main__":
    # sentence = "it was a dark and stormy python"
    list1 = range(2,7)
    # print(list1)
    print(list_of_stars(list1))