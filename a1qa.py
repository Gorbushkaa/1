def file_name():
    print("Введи имя файла")
    try:
        name = str(input())
        with open(name, "r") as file:
            file.readline()
        return name
    except IOError:
        print("Файл не найден")
        file_name()


def number(counter):
    print("Введите {}-e число".format(counter))
    try:
        inp = int(input())
        return inp
    except ValueError:
        print("Это не число!")
        number(counter)


def read_f(num1, num2, name):
    with open(name, "r") as file:
        lines = file.readlines()
        print_line = lines[num1-1:num2]
        del lines[num1-1:num2]
        print(''.join(print_line))
        return lines


def write_f(lines, name):
    with open(name, "w") as file:
        for line in lines:
            file.write(line)


def main():
    name = file_name()
    num1 = number(1)
    num2 = number(2)
    if num1 > num2:
        num1, num2 = num2, num1
    write_f(read_f(num1, num2, name), str(name))


if __name__ == '__main__':
    main()
