import argparse
import sys
from pathlib import path


def main():
    parser = argparse.ArgumentParser()  # 创建一个ArgumentParser对象
    parser.add_argument("--board_grid", type=int,  # 调用add_argument()方法给ArgumentParser添加程序参数信息
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

    if args.board_grid % args.unit_grid != 0:
        sys.exit('不能整除')
    elif len(args.positions) != args.unit_n | args.positions < 1 | args.positions > (args.board_grid/args.unit_grid)**2:
        sys.exit('组件编号有误')
    else:
        path(args.outdir + args.file_name + '.mat')
        path(args.outdir + args.file_name + '.jpg')


if __name__ == "__main__":
    main()
