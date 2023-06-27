# Write your solution here
# def distinct_numbers(my_list):
#     distinct = []
#     for i in my_list:
#         if i not in my_list:
#             distinct.append(i)
#     return (sorted(distinct))

def distinct_numbers(list_1):
    distinct = []
    for i in list_1:
        if i not in distinct:
            distinct.append(i)
        # distinct_2 = sorted
    return sorted(distinct)
    



if __name__ == "__main__":
    my_list = [5, 6, 7, 8, 8, 9, 9, 5]
    print(distinct_numbers(my_list)) # [1, 2, 3]