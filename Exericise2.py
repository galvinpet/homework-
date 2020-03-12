#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
z = []
for a in range(1499, 2701):
    if (a % 7 == 0) and (a % 5):
        z.append(str(a))
print(z)