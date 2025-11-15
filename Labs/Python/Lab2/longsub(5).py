def longest_substring(text):
    longest = text[0]
    current = text[0]

    for i in range(1, len(text)):
        if text[i] >= current[-1]:

            current += text[i]
        else:

            if len(current) > len(longest):
                longest = current

            current = text[i]

    if len(current) > len(longest):
        longest = current

    print("Longest substring in alphabetical order is:", longest)


longest_substring("abdulrahman")
