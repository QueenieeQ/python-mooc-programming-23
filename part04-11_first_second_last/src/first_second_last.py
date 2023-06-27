# # Write your solution here
# # You can test your function by calling it within the following block
# # def first_word(sentence):
# #     return sentence.split()[0]

# # def second_word(sentence):
# #     return sentence.split()[1]

# # def last_word(sentence):
# #     words = sentence.split()
# #     return words[-1]
# def find_word(str, whatth):
#     index = 0
#     word = ""
#     counter = 0
#     while index < len(str):
#     	if str[index] == " ":
#     	    counter += 1
#     	    if counter == whatth:
#     	        break
#     	    word = ""
#     	else:
#     	    word += str[index]
#     	index += 1
#     return word
 
# def first_word(mjono):
#     return find_word(mjono, 1)
 
# def second_word(mjono):
#     return find_word(mjono, 2)
 
# def last_word(mjono):
#     return find_word(mjono, 0)

# if __name__ == "__main__":
#     sentence = "once upon a time there was a programmer"
#     print(first_word(sentence))
#     print(second_word(sentence))
#     print(last_word(sentence))
list=[1, 2, 3 ,4 ,5]
print(len(list))
list.pop(2)
list.remove(1)
print(list)
