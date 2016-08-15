theStrings = {0: "",
              1: "one",
              2: "two",
              3: "three",
              4: "four",
              5: "five",
              6: "six",
              7: "seven",
              8: "eight",
              9: "nine",
              10: "ten",
              11: "eleven",
              12: "twelve",
              13: "thirteen",
              14: "fourteen",
              15: "fifteen",
              16: "sixteen",
              17: "seventeen",
              18: "eighteen",
              19: "nineteen",
              20: "twenty",
              30: "thirty",
              40: "forty",
              50: "fifty",
              60: "sixty",
              70: "seventy",
              80: "eighty",
              90: "ninety",
              100: "hundred",
              1000: "thousand"}


def stringForNumber(n):
    result = ""
    hundreds = (n % 1000) // 100
    tens = (n % 100) // 10
    ones = n % 10

    # 1000
    if n == 1000:
        result = "onethousand"
        return result

    # Hundreds
    if hundreds == 0:
        pass
    else:
        result += theStrings[hundreds]
        result += "hundred"

    # and
    if hundreds > 0 and (tens > 0 or ones > 0):
        result += "and"

    # tens
    if tens == 0:
        pass
    elif tens == 1:
        result += theStrings[n % 100]
        return result
    else:
        result += theStrings[tens * 10]

    # ones
    result += theStrings[ones]

    # final
    return result

counter = 0
for i in range(1000):
    print(i + 1, stringForNumber(i + 1), len(stringForNumber(i + 1)))
    counter += len(stringForNumber(i + 1))
print(counter)
