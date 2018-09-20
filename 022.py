names = []
with open("022_names.txt", "r") as f:
    names = f.readline().split(",")
names = [name[1 : -1] for name in names]
names.sort()

def name_score(idx, name):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    score = 0
    for letter in name.lower():
        score += alphabet.index(letter) + 1
    score *= idx + 1

    return score

overall = sum(name_score(i, name) for (i, name) in enumerate(names))
print(overall)
