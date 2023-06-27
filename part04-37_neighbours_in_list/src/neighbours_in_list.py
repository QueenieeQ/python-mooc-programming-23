def longest_series_of_neighbours(my_list):
    max_length = 0
    current_length = 0
    # print(abs(my_list[3]))
    for i in range(len(my_list) - 1):
        if abs(my_list[i] - my_list[i+1]) == 1:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
    if current_length > max_length:
        max_length = current_length
    return max_length + 1  # Add 1 to include the last element in the series

if __name__ == "__main__":
    my_list = [1, 2, 3, 5, 6, 9, 10]
    print(longest_series_of_neighbours(my_list))
