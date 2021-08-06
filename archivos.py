def read():
    numbers = []
    with open("./archivos/numbers.txt", "r") as f: 
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Byron", "Andres", "Roberto", "Susana", "Maria"]
    with open("./archivos/names.txt", "w") as f:
        for name in names: 
            f.write(name)
            f.write("\n")


def run():
    write()


if __name__ == '__main__':
    run()