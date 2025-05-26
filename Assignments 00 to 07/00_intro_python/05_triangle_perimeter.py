def main():
    print("This program show the perimeter of the triangle")
    
    len1= float(input("\033[1mWhat is the length of side 1?\033[0m"))
    len2 = float(input("\033[1mWhat is the length of side 2?\033[0m"))
    len3 = float(input("\033[1mWhat is the length of side 3?\033[0m"))

    perimeter = len1 + len2 + len3

    print(f"The perimeter of the triangle is: {perimeter}")

if __name__ == '__main__':
    main()


