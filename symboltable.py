# Symbol Table using Dictionary

table = {}

while True:
    print("\n1.Insert  2.Search  3.Delete  4.Display  5.Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        k = input("Token id: ")
        s = input("Symbol: ")
        t = input("Type: ")
        table[k] = (s, t)

    elif ch == '2':
        k = input("Token id: ")
        print(table[k] if k in table else "Not Found")

    elif ch == '3':
        k = input("Token id: ")
        if k in table:
            del table[k]
            print("Deleted successfully")
        else:
            print("No element to delete (ID not found)")

    elif ch == '4':
        if not table:
            print("Symbol table is empty")
        else:
            for k, v in table.items():
                print(k, v)

    elif ch == '5':
        break
