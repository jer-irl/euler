import itertools

def pentag(d):
    return d * (3 * d - 1) // 2

pentags = []
def pentags_up_to_idx(upper_idx):
    global pentags

    for i in range(len(pentags) + 1, upper_idx + 1):
        pentags.append(pentag(i))

    return pentags

def pentags_up_to_upper(upper_val):
    global pentags
    for i in itertools.count(len(pentags) + 1):
        if pentags[-1] > upper_val:
            return pentags
        pentags.append(pentag(i))

best_difference = float("Inf")
for idx in itertools.count(1):
    pentags_up_to_idx(idx + 1)
    if pentags[-1] - pentags[-2] > best_difference:
        break
    bigger_pent = pentags[idx - 1]
    for smaller_pent in pentags[:idx - 1]:
        added = bigger_pent + smaller_pent
        subtracted = bigger_pent - smaller_pent
        pentags_up_to_upper(added)
        if added in pentags and subtracted in pentags:
            if subtracted < best_difference:
                print(subtracted)
                best_difference = subtracted

print(best_difference)

