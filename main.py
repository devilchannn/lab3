def l1():

    num = int(input())
    s = ''

    for i in range(1, num + 1):
        sl = input()
        s = s + sl + ' '
        sl = ''
    print(s)


def l2():

    s = ''
    sl = input()

    while sl != 'stop':
        s = s + sl + ' '
        sl = ''
        sl = input()

    print(s)


def l3():

    sl = input()
    if "ф" in sl or "Ф" in sl:
        print("Слово редкое!")
    else:
        print("Слово не редкое. Как жаль.")

    "3"


def l4():

    import random
    v = 0
    n = 0

    while n != 3 :
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        r = a + b
        ot = input(str(a) + "+" + str(b) + "=")

        if ot == str(r):
            print("Правильно")
            v = v + 1
        else:
            print("Неверно")
            n = n + 1
    print("Игра окончена. Кол-во правильных ответов = ", v)



