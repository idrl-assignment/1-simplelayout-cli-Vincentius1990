import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--board_grid", type=int,
                        help="display the board_grid")
    parser.add_argument("--unit_grid", type=int,
                        help="display the unit_grid")
    parser.add_argument("--unit_n", type=int,
                        help="display the number_of_unit")
    parser.add_argument("--positions", type=int,
                        help="display the positions_of_unit")
    parser.add_argument("-o", "--outdir", type=str,
                        help="display the positions_of_unit")
    parser.add_argument("--file_name", type=str,
                        help="display the positions_of_unit")
    args = parser.parse_args()
    if args.board_grid % args.unit_grid != 0:
        sys.exit()
    elif args.positions < 1 | args.positions > (args.board_grid/args.unit_grid)**2:
        sys.exit()
    else:
        path = r'D:/test'
        os.mkdir(path + args.outdir + args.file_name + '.mat',
                 path + args.outdir + args.file_name + '.jpg')


if __name__ == "__main__":
    main()
