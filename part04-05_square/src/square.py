# Copy here code of line function from previous exercise

def line(Num, string):
        index = 0
        while index < Num:
            print(string * Num)
            index +=1
def square(height,string):
    # You should call function line here with proper parameters
    # while height > 0:
        # line(height)
        line(height, string)
        # height -=1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(3,"x")
