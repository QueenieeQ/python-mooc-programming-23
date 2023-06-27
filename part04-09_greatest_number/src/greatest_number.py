# Write your solution here
# You can test your function by calling it within the following block
def greatest_number(num1, num2, num3):
    greatest = num1
    if num2 > greatest:
        greatest = num2
    if num3 > greatest:
        greatest = num3
    return greatest

# Example usage
# print(greatest_number(3, 4, 1))  # Output: 4

if __name__ == "__main__":
    greatest = greatest_number(41, 5, 5)
    # greatest = greatest_number(-100, 100, -200)
    print(greatest)