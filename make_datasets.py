import random

def write_int_file(path, numbers):
    with open(path, "w") as f:
        for n in numbers:
            f.write(f"{n}\n")

# 1) sorted1000: 1..1000
sorted1000 = list(range(1, 1001))
write_int_file("sorted1000.txt", sorted1000)

# 2) reverse1000: 1000..1
reverse1000 = list(range(1000, 0, -1))
write_int_file("reverse1000.txt", reverse1000)

# 3) random1000: permutation of 1..1000
random1000 = sorted1000[:]
random.shuffle(random1000)
write_int_file("random1000.txt", random1000)

# 4) random2000: permutation of 1..2000
sorted2000 = list(range(1, 2001))
random2000 = sorted2000[:]
random.shuffle(random2000)
write_int_file("random2000.txt", random2000)

# 5) random4000: permutation of 1..4000
sorted4000 = list(range(1, 4001))
random4000 = sorted4000[:]
random.shuffle(random4000)
write_int_file("random4000.txt", random4000)

# 6) almostsorted1000: 1..1000 with a few random swaps
almostsorted1000 = sorted1000[:]
for _ in range(20):  # 20 random swaps
    i, j = random.sample(range(1000), 2)
    almostsorted1000[i], almostsorted1000[j] = almostsorted1000[j], almostsorted1000[i]
write_int_file("almostsorted1000.txt", almostsorted1000)

# 7) duplicates1000: many repeats, 4 distinct values
duplicates1000 = []
values = [1, 2, 3, 4]
for _ in range(1000):
    duplicates1000.append(random.choice(values))
write_int_file("duplicates1000.txt", duplicates1000)

print("Datasets generated:")
print(" - sorted1000.txt")
print(" - reverse1000.txt")
print(" - random1000.txt")
print(" - random2000.txt")
print(" - random4000.txt")
print(" - almostsorted1000.txt")
print(" - duplicates1000.txt")
