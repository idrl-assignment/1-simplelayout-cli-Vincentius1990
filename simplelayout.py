import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--board_grid", type=int,
                        help="the board_grid")
    parser.add_argument("--unit_grid", type=int,
                        help="the unit_grid")
    parser.add_argument("--unit_n", type=int,
                        help="the number_of_unit")
    parser.add_argument("--positions", type=int, nargs='+',
                        help="the positions")
    parser.add_argument("-o", "--outdir", type=str, default='/example_dir',
                        help="the outdir")
    parser.add_argument("--file_name", type=str, default='example',
                        help="the file_name")
    args = parser.parse_args()
    n = args.board_grid/args.unit_grid
    if args.board_grid % args.unit_grid != 0:
        sys.exit('不能整除')
    elif len(args.positions) != args.unit_n:
        sys.exit('组件数量错误')
    elif min(args.positions) < 1 | max(args.positions) > n**2:
        sys.exit('组件编号超出范围')
    else:
        Path(args.outdir).mkdir(parents=True, exist_ok=True)
        with open(args.outdir + '/' + args.file_name + '.mat', 'w') as f1:
            pass
        with open(args.outdir + '/' + args.file_name + '.jpg', 'w') as f2:
            pass
        print('done')


if __name__ == "__main__":
    main()
