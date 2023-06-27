def count_matching_elements(my_matix, element):
    # print(my_matix)
    count =0
    for row in my_matix:
        for num in row:
            if num == target_element:
                count += 1
    return count

if __name__ == "__main__":
    m = [[1, 2, 3], [2, 3, 1], [4, 5, 6]]
    target_element = 2
    result2 = count_matching_elements([[2, 2, 2, 4, 5, 1], [3, 3, 4, 4, 2, 3], [1, 4, 3, 4, 4, 4], [3, 4, 3, 1, 4, 5]], 1)
    result = count_matching_elements(m, target_element)
    print(result2)
    print(result)  # Output: 2
