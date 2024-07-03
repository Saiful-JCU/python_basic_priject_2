# solution 1
string = input("")
if string == "":
    print("empty")
else:
    for i in range(len(string)):
        if i % 2 == 0:
            print(string[i])



# solution 1
txt = input()
if len(txt) == 0:
    print("empty")
else:
    for i in range(0, len(txt), 2):
        print(txt[i])