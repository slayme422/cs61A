"""
运用的所有变量
solve_hanoi(n , start_peg, end_peg)
运行:转移n个disk，从第start_peg个柱子到第end_peg上
    例如:solve_hanoi(2,1,3)
        转移2个disk，从第1个柱子到第3个柱子上

    n:代表的是disk的数量
    start_peg:起始柱子
    end_peg:目的柱子

    (3,1,2)->(2,1,3)
"""   
def solve_hanoi(n, start_peg, end_peg):
    #base case
    if(n==1):
        move_disk(n, start_peg, end_peg)

    else:
        spare_peg=6-start_peg-end_peg
        solve_hanoi(n-1, start_peg, spare_peg)
        move_disk()
        solve_hanoi(n-1,end_peg,start_peg)


def move_disk(disk_number, start_peg, target_peg):
    print(f"move {disk_number} from {start_peg} to {target_peg}")



