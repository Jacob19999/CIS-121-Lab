
#1
def skip_letter(word):
    result = []
    for i in range(0, len(word), 2):
        result.append(word[i])
    return result

print(skip_letter("counterattack"))
print(skip_letter("banana sunday"))

#2
def skip_letter2(word):
    result = []
    for i in range(1, len(word), 2):
        result.append(word[i])
    return result

print(skip_letter2("counterattack"))
print(skip_letter2("banana sunday"))

#3
def even_numbers(smaller_num, larger_num):
    result = []
    for num in range(smaller_num, larger_num + 1):
        if num % 2 == 0:
            result.append(num)
    return result

print(even_numbers(37, 1050))
print(even_numbers(1, 2000))
print(even_numbers(50, 199))

#4
def odd_numbers(smaller_num, larger_num):
    result = []
    for num in range(smaller_num, larger_num + 1):
        if num % 2 == 1:
            result.append(num)
    return result

print(odd_numbers(37, 1050))
print(odd_numbers(1, 2000))
print(odd_numbers(50, 199))

#5
def hailstone_seq(n):
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        result.append(n)
    return result

print(hailstone_seq(25))
print(hailstone_seq(40))

#6
def find_factors(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result

print(find_factors(12))
print(find_factors(17))
print(find_factors(36))

#7
def ascending_order(num1, num2, num3):
    numbers = [num1, num2, num3]
    smallest = numbers[0]
    if numbers[1] < smallest:
        smallest = numbers[1]
    if numbers[2] < smallest:
        smallest = numbers[2]
    middle = None
    if smallest == num1:
        remaining = [num2, num3]
    elif smallest == num2:
        remaining = [num1, num3]
    else:
        remaining = [num1, num2]
    middle = remaining[0]
    if remaining[1] < middle:
        middle = remaining[1]
    largest = num1 + num2 + num3 - smallest - middle
    return [smallest, middle, largest]

print(ascending_order(2, 3, 1))
print(ascending_order(10, 1, 25))
print(ascending_order(2, 45, 4))

#8
def descending_order(num1, num2, num3):
    numbers = [num1, num2, num3]
    largest = numbers[0]
    if numbers[1] > largest:
        largest = numbers[1]
    if numbers[2] > largest:
        largest = numbers[2]
    middle = None
    if largest == num1:
        remaining = [num2, num3]
    elif largest == num2:
        remaining = [num1, num3]
    else:
        remaining = [num1, num2]
    middle = remaining[0]
    if remaining[1] > middle:
        middle = remaining[1]
    smallest = num1 + num2 + num3 - largest - middle
    return [largest, middle, smallest]

print(descending_order(2, 3, 1))
print(descending_order(10, 1, 25))
print(descending_order(2, 45, 4))

#9
def count(cards):
    total = 0
    for card in cards:
        if card in ['2', '3', '4', '5', '6']:
            total += 1
        elif card in ['10', 'J', 'Q', 'K', 'A']:
            total -= 1
    return total

print(count([5, 9, 10, 3, 'J', 'A', 4, 8, 5]))
print(count(['A', 'A', 'K', 'Q', 'Q', 'J']))
print(count(['A', 5, 5, 2, 6, 2, 3, 8, 9, 7]))

#10
def war_of_numbers(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    if even_sum > odd_sum:
        return "evens"
    else:
        return "odds"

print(war_of_numbers([2, 8, 7, 5]))
print(war_of_numbers([12, 90, 75, 1, 1]))
print(war_of_numbers([2, 10, 22, 243]))

#11
def add_lists(lyst1, lyst2):
    result = []
    for i in range(len(lyst1)):
        sum_val = lyst1[i] + lyst2[i]
        result.append(sum_val)
    return result

print(add_lists([1, 3, 3, 1], [4, 3, 6, 1]))
print(add_lists([1, 8, 5, 0, -7], [0, -7, 4, 2, -6]))
print(add_lists([1, 2], [-1, 1]))

#12
def largest_even(numbers):
    max_even = -1
    for num in numbers:
        if num % 2 == 0 and num > max_even:
            max_even = num
    return max_even

print(largest_even([3, 7, 2, 1, 7, 9, 10, 13]))
print(largest_even([1, 3, 5, 7]))
print(largest_even([0, 19, 18973623]))

#13
def largest_odd(numbers):
    max_odd = -1
    for num in numbers:
        if num % 2 == 1 and num > max_odd:
            max_odd = num
    return max_odd

print(largest_odd([3, 7, 2, 1, 7, 9, 10, 13]))
print(largest_odd([2, 4, 6, 8]))
print(largest_odd([0, 19, 18973623]))

#14
def progress_days(miles):
    count = 0
    for i in range(1, len(miles)):
        if miles[i] > miles[i-1]:
            count += 1
    return count

print(progress_days([3, 4, 1, 2]))
print(progress_days([10, 11, 12, 9, 10]))
print(progress_days([6, 5, 4, 3, 2, 9]))
print(progress_days([9, 9]))

#15
def lag_days(miles):
    count = 0
    for i in range(1, len(miles)):
        if miles[i] < miles[i-1]:
            count += 1
    return count

print(lag_days([5, 3, 2, 1]))
print(lag_days([10, 11, 12, 9, 10]))
print(lag_days([6, 5, 4, 3, 2, 9]))
print(lag_days([9, 9]))

#16
def like_or_dislike(events):
    state = "nothing"
    for event in events:
        if event == "like":
            if state == "like":
                state = "nothing"
            elif state == "dislike":
                state = "like"
            else:
                state = "like"
        elif event == "dislike":
            if state == "dislike":
                state = "nothing"
            elif state == "like":
                state = "dislike"
            else:
                state = "dislike"
    return state

print(like_or_dislike(["dislike"]))
print(like_or_dislike(["like", "like"]))
print(like_or_dislike(["dislike", "like"]))
print(like_or_dislike(["like", "dislike", "dislike"]))

#17
def get_indices(lyst, item):
    indices = []
    for i in range(len(lyst)):
        if lyst[i] == item:
            indices.append(i)
    return indices

print(get_indices([1, 5, 5, 2, 7], 7))
print(get_indices([1, 5, 5, 2, 7], 5))
print(get_indices([1, 5, 5, 2, 7], 8))
print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))

#18
def list_of_multiples(num, length):
    result = []
    current = num
    while len(result) < length:
        result.append(current)
        current += num
    return result

print(list_of_multiples(7, 5))
print(list_of_multiples(12, 10))
print(list_of_multiples(17, 6))

#19
def is_acronym(s, words):
    if len(s) != len(words):
        return False
    acronym = ""
    for word in words:
        if len(word) == 0:
            return False
        acronym += word[0]
    return s == acronym

print(is_acronym("abc", ["alice", "bob", "charlie"]))
print(is_acronym("a", ["an", "apple"]))
print(is_acronym("ngguoy", ["never", "gonna", "give", "up", "on", "you"]))
print(is_acronym("ab", ["apple", "banana", "cat"]))
print(is_acronym("ab", ["apple", "", "cat"]))
