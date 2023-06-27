# Write your solution here
def everything_reversed(local_list : list):
    new_list = []
    for i in local_list[::-1]:
        new_list.append(i[::-1])
        # print(local_list[::-1])

        # new_list.insert(0,i)
        # for j in new_list:
            # print(new_list[::-1])
    return new_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)