def encode_message(message):
    encoded_string = ""
    i = 0
    while i <= len(message) - 1:
        count = 1
        ch = message[i]
        j = i
        while j < len(message) - 1:
            # The count will increment if the symbol in current and
            # next position are the same
            if message[j] == message[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        # For every symbol change we attach the number of the count and the symbol
        encoded_string = encoded_string + str(count) + ch
        i = j + 1

        # Returning the final string without repetition os consequent symbols.
    return encoded_string
