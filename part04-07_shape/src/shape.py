# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(tri_num, tri_string, rectangle_num, rectangle_string):
    index = 0
    hashes = (tri_num * tri_string)
    while index <= tri_num:
        print(hashes[0:index])
        index += 1
    # print(rectangle_num * rectangle_string)    
    # while index == tri_num:
    index2 = 0
    while index2 < rectangle_num:
        print(tri_num * rectangle_string)
        index2 +=1
        # index +=1

def shape(tri_num, tri_string, rectangle_num, rectangle_string):
    line(tri_num, tri_string, rectangle_num, rectangle_string)
if __name__ == "__main__":
    shape(5, "x", 3, "*")