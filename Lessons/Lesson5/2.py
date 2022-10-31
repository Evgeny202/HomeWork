lol_input = ["rus", "eng", "jap", "rus", "eng"]
lol_set = set(lol_input)
lol_list = list(lol_set)
print(lol_input == lol_list)
for i in lol_list:
    if i in lol_input:
        a = lol_input.remove(i)
print(lol_input)