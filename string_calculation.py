def string_sum(word):
    result = 0
    temp=''
    for char in word:
        if char.isdigit():
            temp+=char
        else:
            if temp:
                result+=int(temp)
                temp=''
    if temp:
        result+=int(temp)
    return result

print(string_sum(input("Enter the string: ")))
    