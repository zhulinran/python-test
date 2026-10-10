tasks = []
""""任务列表，用来收集任务和排列任务"""
def show_menu():
    print("----------------控制台菜单----------------")
    print("1添加任务")
    print("2查看全部")
    print("3标记完成")
    print("4删除任务")
    print("5搜索与筛选")
    print("6统计")
    print("7保存数据")
    print("8导出报告")
    print("9退出系统")
    print("=========================================")
def main():

    #后面有用，用来读取上一次程序保存的数据
    while True:
        show_menu()
        choice = input("请输入您的操作编号：")
        if choice == "9":
            print("感谢使用，再见！")
            break
        elif choice == "2":#查看全部
            print("========全部任务清单========")
            if len(tasks) == 0:
                print("当前订单为空")
            else:
                for task in tasks:
                    task.show_info()


        elif choice == "3":
                    mark_num = input("请输入要标记完成的任务标号")
                    found = False
                    for task in tasks:
                        if task.num == mark_num:
                            task.status = "已完成"
                            print("任务已标记完成")

                            break
                    if not found:
                        print("没有找到该编号的任务")

class task:
       def __init__(self,num,level,deadline,status):
        self.num = num
        self.level = level
        self.deadline = deadline
        self.status = status

def show_info(self):
        print("======待办清单======")
        print(f"编号{self.num}")
        print(f"等级{self.level}")
        print(f"截止日期{self.deadline}")
        print(f"状态{self.status}")
tests = []
main()