from argparse import ArgumentParser

def main() -> None:
    parser = ArgumentParser(prog="dtb-converter", description="Convert decimal to binary")
    
    parser.add_argument("number", type=int)

    args = parser.parse_args()

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

if __name__ == "__main__":
    main()