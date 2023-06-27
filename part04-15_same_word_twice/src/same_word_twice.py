# Write your solution here
list_blank = []
while True:
    string_input = input("Word:")
    if string_input in list_blank:
        break
    list_blank.append(string_input)
print(f"You typed in {len(list_blank)} different words")

