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
        elif choice == "1":
            add_task()
        elif choice == "4":
            delete_task()
def add_task():
    print("-----------------添加任务----------------")
    title = input("请输入任务标题：").strip()                        #.strip()是用来去除开头和末尾的空格的
    if title == "":
        print("标题不能为空！")
        return
    priority = input("请输入优先级（高/中/低）：").strip()
    if priority not in ["高", "中", "低"]:
        print("优先级必须是 高/中/低 其中一个！")
        return
    deadline = input("请输入截止日期（格式：2026-10-09）：").strip()     #目前还不能对那些不正确的月份进行甄别
    if len(deadline) != 10 or deadline[4] != "-" or deadline[7] != "-":
        print("日期格式不对！必须是 2026-10-09 这样的格式")              #这里也可以优化，要求重问，选择是否重新输入日期，否的话返回
        return
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "title": title,
        "priority": priority,
        "deadline": deadline,
        "status": "未完成"
    }
    tasks.append(task)                                #将新的任务储存到tasks字典的最末端
    print(f"添加成功！任务信息如下：")
    print(f"编号：{task['id']}")
    print(f"标题：{task['title']}")
    print(f"优先级：{task['priority']}")
    print(f"截止日期：{task['deadline']}")
    print(f"状态：{task['status']}")
def delete_task():
    """删除一个任务。
        流程：显示所有任务 → 输入编号 → 校验数字 → 查找任务 → 二次确认(y/n) → 删除并重新编号
        参数：无
        返回：无
        """
    print("-------------------删除任务-------------------")   #这个开头后面可以修改一下，对齐或者其他形式
    if len(tasks) == 0:
        print("暂无任务可删除！")
        return
    print("当前任务列表：")
    for task in tasks:
        print(f"编号：{task['id']} | 标题：{task['title']}")
    task_id = input("请输入您想要删除任务的编号：").strip()
    if not task_id.isdigit():                         #这玩意是用来检验是否全是数字
        print("请输入数字编号！！！")
        return
    task_id = int(task_id)
    found = False
    for i in range(len(tasks)):
        if tasks[i]["id"] == task_id:
            while True:
                confirm = input(f"确定要删除任务「{tasks[i]['title']}」吗？(y/n)：").strip().lower()
                #lower可以使输入进来的全变成小写，这样输入大写的Y,N也没事
                if confirm == "y":
                    del tasks[i]
                    for j in range(len(tasks)):
                        tasks[j]["id"] = j + 1
                    print("删除成功，已帮您更新了最新数据！")
                    break

                elif confirm == "n":
                    print("已取消删除。")
                    break

                else:
                    print("输入有误，请输入 y 或 n！")

            found = True
            break
    if not found:
        print(f"没有找到编号为 {task_id} 的任务！")
main()


