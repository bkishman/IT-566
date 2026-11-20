###Entry point for Database Project###

from expense_tracker import expense_tracker
import yaml
from argparse import ArgumentParser

def main():
    args = configure_and_parse_command_line_arguments()
    if args.configfile:
        config = None
        with open(args.configfile, 'r') as f:
            config = yaml.load(f.read(), Loader=yaml.SafeLoader)
        print(f'{config}')
    expense_tracker.run()

#Configure and parse CLI arguments
def configure_and_parse_command_line_arguments():
    parser = ArgumentParser(
        prog="main.py",
        description="Start Expenses Application from Configuration File",
        epilog="POC: Ben Kishman"
    )
    parser.add_argument("-c", "--configfile", help="Configuration File to Load", required=True)

    args = parser.parse_args()
    return args
        
if __name__ == "__main__":
    main()