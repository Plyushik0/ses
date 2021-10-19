s = 9**8 + 3**24 - 18
print(s)
string = ""
while (s > 0):
    string = str(s % 3) + string
    s = s // 3
print(string.count("2"))
input()