#This program prints the initial letters of the user's name
#This program is created by Ann

name = input("Enter your name: ")
len_name = len(name)
total = ''
for i in range (len(name)):
    if name[i] == " ":
        total = total + (name[i + 1])
print(name[0] + total)
