def main():
    number = float(input("\033[1mType a number to see its square:\033[0m"))

    square= number * number

    print(f"{number} squared is: {square}")

if __name__ == '__main__':
    main()