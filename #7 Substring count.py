print("This program will print how many times 'Emma' is in the sentence.")
str_x = "Emma is a good developer. Emma is a writer"
print(str_x)

times = 0

for words in str_x.split():
    if words == "Emma":
        times += 1

print(f"Emma appeared {times} times")

