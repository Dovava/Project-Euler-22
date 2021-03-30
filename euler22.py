values = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,
          "K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,
          "U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
f = open("names.txt","r")
names = f.read(1000000)
names = names.replace('"', "")
namelist = names.split(",")
namenum = 1
scores = []
answer = 0
namelist = sorted(namelist)
for name in namelist:
    score = 0
    for letter in name:
        score += values[letter]
    scores.append(score*namenum)
    score = 0
    namenum += 1
for score in scores:
    answer += score
print(answer)
