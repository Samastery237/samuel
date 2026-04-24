def main():
    x = get_in()
    print(f"x is {x}")


def get_in():
    while True:
        try:
            return int(input("What's x?"))            
        except ValueError:
            pass


main()
