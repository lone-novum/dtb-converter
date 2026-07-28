from argparse import ArgumentParser

def main() -> None:
    parser = ArgumentParser(prog="dtb-converter", description="Convert decimal to binary")
    
    parser.add_argument("number")

    args = parser.parse_args()

if __name__ == "__main__":
    main()