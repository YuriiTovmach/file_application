# file name
FILENAME = "messages.txt"
# define empty list
messages = list()

for i in range(4):
    message = input("Enter the string " + str(i + 1) + ": ")
    messages.append(message + "\n")

# write list to file
with open(FILENAME, "a") as file:
    for message in messages:
        file.write(message)

# read messages from file
print("Read messages")
with open(FILENAME, "r") as file:
    for message in file:
        print(message, end="")