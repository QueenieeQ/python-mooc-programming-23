# Copy here code of line function from previous exercise
def line(num, string):
    index = 0
    hashes = (num * string)
    while index <= num:
        print(hashes[0:index])
        index += 1
def triangle(size):
    # You should call function line here with proper parameters
    # while size > 0 : 
        line(size, "#")
        # print()
        # size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
