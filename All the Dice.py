import D4
import D6
import D8
import D10
import D12
import D20


def main():
    selection = int(input("Enter 1 for D4, 2 for D6, 3 for D8, 4 for D10, 5 for D12, 6 for D20: "))

    if selection == 1:
        D4.d4_dice()
    elif selection == 2:
        D6.d6_dice()
    elif selection == 3:
        D8.d8_dice()
    elif selection == 4:
        D10.d10_dice()
    elif selection == 5:
        D12.d12_dice()
    elif selection == 6:
        D20.d20_dice()
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()