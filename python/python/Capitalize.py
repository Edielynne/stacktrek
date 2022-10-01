def capitalize (str):
    new_string=""
    previous_string = ""
    previous_two_string = ""
    char = 0
    counter = 0
    for char in str:
        if (previous_two_string == "!" or previous_two_string == "." or previous_two_string == "?") and previous_string == " ":
            new_string = new_string + char.upper()
        elif previous_string == "!" or previous_string == "." or previous_string == "?":
            new_string = new_string + char.upper()
        elif counter == 0:
            new_string = new_string + char.upper()
        else:
            new_string = new_string + char
        previous_two_string = previous_string
        previous_string = char
        counter += 1
    final = new_string.replace(" i ", " I ")
    return final
print(capitalize('It is,i,recon'))