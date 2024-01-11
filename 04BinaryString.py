#wap to check whether a given string is binary or not
def is_binary(string):
    valid_digits = {'0', '1'}
    return all(char in valid_digits for char in string)
input_string = input("Enter a string: ")
if is_binary(input_string):
    print("The given string is binary.")
else:
    print("The given string is not binary.")
