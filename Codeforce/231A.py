x = input()
n = 0
num = 0
while(n < int(x)):
    team = input()
    teamlist = team.split(" ")
    counter = 0
    for i in teamlist:
        if int(i) == 1:
            counter += 1
    if counter >= 2:
        num += 1
    n += 1
print(num)