# Write your solution here
def formatted(my_list):
    formatted =[]
    # new_format = []
    for i in my_list:
        # new_format = "{:.2f}".format(i)
        
        formatted.append(f"{i:.2f}")
    # print(f"The number is {formatted:.2f}")
    return formatted


if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)