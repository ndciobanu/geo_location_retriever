import argparse


def main(args):
    None

    
    
if __name__ == "__main__":
    aparser = argparse.ArgumentParser(
                         description="Geo location "\
                         +"retriever arg parser")
    aparser.add_argument("--address", metavar="Street address",
                         help = "Enter a physical address")
    aparser.add_argument("--file", metavar="List of addresses file",
                         help = "Enter a file name with a list of "\
                         +"addresses, one per line")
    args = aparser.parse_args()
    main(args)
