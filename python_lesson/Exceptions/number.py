def main():
    x = get_in("What'scat x? ")
    print(f"x is {x}")


def get_in(prompt):
    while True:
        try:
            return int(input("What's x? "))            
        except ValueError:
            pass


main()
