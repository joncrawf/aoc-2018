def react(start_string):
    string = []

    for char in start_string:
        if len(string) > 0 and char != string[-1] and char.lower() == string[-1].lower():
           string.pop()
        else:
           string.append(char)

    return ''.join(string)
