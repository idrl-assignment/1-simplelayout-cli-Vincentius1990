import argparse
import sys
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--board_grid", type=int, 
                        help="the board_grid")
    parser.add_argument("--unit_grid", type=int,
                        help="the unit_grid")
    parser.add_argument("--unit_n", type=int,
                        help="the number_of_unit")
    parser.add_argument("--positions", type=int, 
                        help="the positions")                       
    parser.add_argument("-o", "--outdir", type=str,
                        help="the outdir")
    parser.add_argument("--file_name", type=str, default='example',
                        help="the file_name")
    args = parser.parse_args()
    n = args.board_grid/args.unit_grid
    if args.board_grid % args.unit_grid != 0:
        sys.exit()
    elif args.positions < 1 | args.positions > n**2:
        sys.exit()
    else:
        path = r'D:/test'
        os.mkdir(path + args.outdir + args.file_name + '.mat',
                 path + args.outdir + args.file_name + '.jpg')


if __name__ == "__main__":
    main()
