"""Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?
Your puzzle input is 1113222113."""


def recursive_look_and_say(starting_sequence, iterations):
    if iterations == 0:
        return starting_sequence
    else:
        newstr = ""
        buffer = []
        for char in starting_sequence:
            if char in buffer:
                buffer.append(char)
            elif buffer == []:
                buffer.append(char)
            elif char not in buffer:
                newstr = newstr + str(len(buffer)) + buffer[0]
                buffer = [char]
        newstr = newstr + str(len(buffer)) + buffer[0]
        starting_sequence = newstr
        iterations -= 1
        return recursive_look_and_say(starting_sequence, iterations)
