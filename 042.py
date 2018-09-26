with open('042_words.txt', 'r') as f:
    words = f.read()
words = words.split(',')
words = [w.strip('"') for w in words]

max_len_of_word = len(max(words, key=lambda w: len(w)))
max_possible_word_sum = max_len_of_word * 26

# Generate triangle numbers up to max possible word_sum
triangle_nums = set()
for i in range(1, max_possible_word_sum + 1):
    triangle_nums.add(i * (i + 1) // 2)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = list(alphabet)

def sum_of_word(word):
    return sum(alphabet.index(letter) + 1 for letter in word)

num_summing_to_triangle = 0
for word in words:
    if sum_of_word(word) in triangle_nums:
        num_summing_to_triangle += 1

print(num_summing_to_triangle)

