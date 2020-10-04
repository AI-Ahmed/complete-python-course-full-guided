__author__ = "Crypto"

IP = input("Enter your IP address: ")
if IP[-1] != '.':
    IP += '.'
segment = 1  # <--- although the enter was NULL, at least there's one char
charInSeg = 0
character = " "

for character in IP:
    if character == '.':
        print("Segment {} contains {} characters".format(segment, charInSeg))
        segment += 1
        charInSeg = 0
    else:
        charInSeg += 1
# # unless the final character in the string was a . then we haven't printed the last segment
# if character != '.':
#     print("Segment {} contains {} characters".format(segment, charInSeg))


# For a long segment of input msg. you can use '\' to enter a next line
input_prompt = "Please enter an IP Address. An IP address consists of 4 numbers, " \
               "separated from each other with a full stop: "
ipAddress = input(input_prompt)
