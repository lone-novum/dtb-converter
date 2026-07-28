from argparse import ArgumentParser

def main() -> None:
    parser = ArgumentParser(prog="dtb-converter", description="Convert decimal and binary numbers", epilog="Converts to binary on default.")
    
    parser.add_argument("number", type=int)
    parser.add_argument("-d", "--decimal", action="store_true", help="Convert binary to decimal")

    args = parser.parse_args()

    if args.decimal:
        out = convert_to_decimal(args.number)
        print(out)
    else:
        out = convert_to_binary(args.number)
        print(out)

def convert_to_binary(num:int):
    rem = 0
    res = ""
    while num > 0:
        rem = num % 2
        num = num // 2
        res = str(rem) + res
    return res

def convert_to_decimal(num:int):
    exp = len(str(num)) - 1
    res = ""
    x = 0
    for i in str(num):
        if i in '10':
            i = int(i) * (2**exp)
            x += i
            exp -= 1
        else:
            return "Invalid input. Binary number expected."
            break
    res += str(x)
    return res

if __name__ == "__main__":
    main()