def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Перемістити диск з {source} на {target}: {n}")
        disks[source].pop()
        disks[target].append(n)
        print("Проміжний стан:", disks)
        return

    hanoi(n - 1, source, auxiliary, target)
    print(f"Перемістити диск з {source} на {target}: {n}")
    disks[source].pop()
    disks[target].append(n)
    print("Проміжний стан:", disks)
    hanoi(n - 1, auxiliary, target, source)


if __name__ == "__main__":
    n = 3
    disks = {
        "A": list(val for val in range(n, 0, -1)),
        "B": [],
        "C": []
    }

    print("Початковий стан:", disks)
    hanoi(n, 'A', 'B', 'C')
    print("Кінцевий стан:", disks)
