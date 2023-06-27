# Copy here code of line function from previous exercise

def line(Num):
        index = 0
        while index < Num:
            print("#"*Num)
            index +=1
def square_of_hashes(height):
    # You should call function line here with proper parameters
    # while height > 0:
        line(height)
        # height -=1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(3)
