import itertools

running_sum = 0

side_len = 1001

idx_within_run = -1
number_per_run = 0
run_idx = 3

counter = itertools.count()
next(counter)

for x in counter:
    if idx_within_run == number_per_run - 1:
        running_sum += x
        idx_within_run = 0
        if run_idx == 3:
            run_idx = 0
            number_per_run += 2
            if number_per_run > side_len - 1:
                break
        else:
            run_idx += 1
    else:
        idx_within_run += 1

print(running_sum)

