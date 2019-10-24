def number1():
    print("Введите 1-е число")
    try:
        inp = int(input())
        return inp
    except ValueError:
        print("Это не число!")
        number1()


def number2():
    print("Введите 2-е число")
    try:
        inp = int(input())
        return inp
    except ValueError:
        print("Это не число!")
        number2()


def readf(num1, num2):
    with open("1.txt", "r") as file:
        lines = file.readlines()
        print_line = lines[num1-1:num2]
        del lines[num1-1:num2]
        print(''.join(print_line))
        return lines


def writef(lines):
    with open("1.txt", "w") as file:
        for line in lines:
            file.write(line)


def main():
    num1 = number1()
    num2 = number2()
    if num1 > num2:
        num1, num2 = num2, num1
    writef(readf(num1, num2))


if __name__ == '__main__':
    main()
