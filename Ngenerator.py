import random, string

amount = int(input(' Amount of nhentai codes: '))
value = 1
while value <= amount:
    code = "https://nhentai.to/g/" + ('').join(random.choices(string.digits, k=7))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[B3XE] {code}')
    value += 1