import random

num100 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
ran50 = []
ran25 = []
ran15 = []
ran10 = []
ran5 = []
ran3 = []
ran2 = []
final = []
for i in range(1, 51):
    i = random.choice(num100)
    ran50.append(i)
    num100.remove(i)

for i in range(1, 26):
    i = random.choice(ran50)
    ran25.append(i)
    ran50.remove(i)
    
for i in range(1, 16):
    i = random.choice(ran25)
    ran15.append(i)
    ran25.remove(i)
    
for i in range(1, 11):
    i = random.choice(ran15)
    ran10.append(i)
    ran15.remove(i)
    
for i in range(1, 6):
    i = random.choice(ran10)
    ran5.append(i)
    ran10.remove(i)

for i in range(1, 4):
    i = random.choice(ran5)
    ran3.append(i)
    ran5.remove(i)
    
for i in range(1, 3):
    i = random.choice(ran3)
    ran2.append(i)
    ran3.remove(i)
    
for i in range(1, 2):
    i = random.choice(ran2)
    final.append(i)
    ran2.remove(i)
    
for i in range(0, 1):
	i = int(random.choice(final))
	final = i
print(final)
