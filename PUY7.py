
#1
my_dict = {
    1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee',
    7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}
}

print(min(my_dict) + max(my_dict))

#2
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
names = []

for user in users:
    if user['phone'].strip()[-1] == '8':
        names.append(user['name'])

names.sort()
print(" ".join(names))

#3
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
names = []

for user in users:
    if user['email'].strip() == '':
        names.append(user['name'])

names.sort()
print(" ".join(names))
#4
numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

n = input("Введите число: ")
a = [numbers[i] for i in n]  
print(" ".join(a))
#5
courses = {
    "CS101" : ["3004","Хайнс","8:00"],
    "CS102" : ["4501","Альварадо","9:00"],
    "CS103" : ["6755","Рич","10:00"],
    "NT110" : ["1244","Берк","11:00"],
    "CM241" : ["1411","Ли","13:00"]
}
course=input().strip()
room,teacher,time=courses[course]
print(f"{course}: {room}, {teacher}, {time}")
#6
mapping = {
    '.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
    'A': '2', 'B': '22', 'C': '222',
    'D': '3', 'E': '33', 'F': '333',
    'G': '4', 'H': '44', 'I': '444',
    'J': '5', 'K': '55', 'L': '555',
    'M': '6', 'N': '66', 'O': '666',
    'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
    'T': '8', 'U': '88', 'V': '888',
    'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
    ' ': '0'
}

text = input()
result = ""

for ch in text.upper():
    if ch in mapping:
        result += mapping[ch]

print(result)
#7
morse = {
    "A": ".-",     "B": "-...",   "C": "-.-.",   "D": "-..",
    "E": ".",      "F": "..-.",   "G": "--.",    "H": "....",
    "I": "..",     "J": ".---",   "K": "-.-",    "L": ".-..",
    "M": "--",     "N": "-.",     "O": "---",    "P": ".--.",
    "Q": "--.-",   "R": ".-.",    "S": "...",    "T": "-",
    "U": "..-",    "V": "...-",   "W": ".--",    "X": "-..-",
    "Y": "-.--",   "Z": "--..",
    "0": "-----",  "1": ".----",  "2": "..---",  "3": "...--",
    "4": "....-",  "5": ".....",  "6": "-....",  "7": "--...",
    "8": "---..",  "9": "----."
}

text = input().upper()  # переводим в верхний регистр

result = []

for ch in text:
    if ch in morse:
        result.append(morse[ch])  # добавляем код
    # если символа нет в словаре — игнорируем

print(" ".join(result))
#8
result = {}

for i in range(11, 15 + 1):
    result[i] = i ** 2

#9
from collections import Counter

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = dict(Counter(dict1) + Counter(dict2))
#10
#11
words = s.split()
counts = {}

for w in words:
    counts[w] = counts.get(w, 0) + 1

max_count = max(counts.values())
candidates = [word for word, cnt in counts.items() if cnt == max_count]

print(sorted(candidates)[0])
#12
from collections import defaultdict

result = defaultdict(list)

for dog, name, sur, age in pets:
    result[(name, sur, age)].append(dog)
#13
    text = input().lower()

for char in '.,!?:;-':
    text = text.replace(char, ' ')

words = text.split()

stats = {}
for w in words:
    stats[w] = stats.get(w, 0) + 1

min_count = min(stats.values())
rare = sorted([w for w, c in stats.items() if c == min_count])

print(rare[0])
#14
