def no_shouting(another_list):
    normal_list = []
    # print(another_list)
    for item in another_list:
        # print(item.isupper())
        if item.isupper() != True:
            normal_list.append(item)
    # print(normal_list)
    return normal_list

#
#  Write your solution here
if __name__ == "__main__":
    # print("XYZ".isupper())
    # is_it_upper = "Abc".isupper()
    # print(is_it_upper)
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    # print(my_list)
    pruned_list = no_shouting(my_list)
    print(pruned_list)
