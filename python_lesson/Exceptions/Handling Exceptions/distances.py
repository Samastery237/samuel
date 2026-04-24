distances = {
    "Voyage 1": 163,
    "Voyage 2": 136,
    "Pioneer 10": "80 AU",
    "New Horizon": 58,
    "Pioneer 11": "44 AU",
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' is not resgistered in the space system")
        return
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return
    
    m = convert(au)
    print(f"{m} m away")

def convert(au):
    return au * 1495978707000


main()