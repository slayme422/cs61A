def start_game():
    print("欢迎来到文本冒险游戏！")
    current_room = "入口"
    inventory = []  # 你的背包，存物品

    while True:
        if current_room == "入口":
            print("\n你站在黑暗的入口处。")
            print("选项：1. 进入大厅  2. 退出游戏")
            choice = input("请输入选项编号：")

            if choice == "1":
                current_room = "大厅"
            elif choice == "2":
                print("游戏结束，谢谢游玩！")
                break
            else:
                print("无效选项，请重新输入。")

        elif current_room == "大厅":
            print("\n你到了大厅。")
            print("选项：1. 捡起钥匙  2. 进入宝藏室  3. 返回入口")
            choice = input("请输入选项编号：")

            if choice == "1":
                if "钥匙" not in inventory:
                    print("你捡起了一把钥匙！")
                    inventory.append("钥匙")
                else:
                    print("你已经有钥匙了。")
            elif choice == "2":
                if "钥匙" in inventory:
                    current_room = "宝藏室"
                else:
                    print("宝藏室门锁着，你需要钥匙。")
            elif choice == "3":
                current_room = "入口"
            else:
                print("无效选项，请重新输入。")

        elif current_room == "宝藏室":
            print("\n你进入了宝藏室，发现了很多宝藏！恭喜你赢了！")
            break

if __name__ == "__main__":
    start_game()

def repeat(f,n,x):
    if n==1:
        return 1
    return f(x) * repeat(f,n-1,x)

print(repeat(lambda x:x*x,2,5))