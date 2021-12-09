def decode(our_message):
    decoded_message = ""
    i = 0
    j = 0
    # Differentiating counts from words (previously defined in encoding function)
    while i <= len(our_message) - 1:
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        # displaying the character multiple times specified by the count
        for j in range(run_count):
            # Repeat word the defined amount of times and concatenate to the string
            decoded_message = decoded_message + run_word
            j = j + 1
        i = i + 2
    return decoded_message
