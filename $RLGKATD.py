from datetime import datetime       #引入datetime模块来帮助判断日期格式是否规范
from random import choice
from re import search
from unittest import result
today_str = datetime.now().strftime("%Y-%m-%d")
tasks = []     #任务列表，用来收集任务和排列任务
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
    load_data()                                                       #用来读取上一次程序保存的数据
    while True:
        show_menu()
        choice = input("请输入您的操作编号：")
        if choice == "9":
            print("感谢使用，再见！")
            break
        elif choice == "1":
            add_task()
        elif choice == "2":
            show_info()
        elif choice == "3":
            task_mark()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            search_task()
        elif choice == "7":
            save_data()
        else:
            print("输入有误，请重输")
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
    deadline= input("请输入截止日期（格式：2026-10-09）：").strip()
    try:
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("日期格式不对或日期不存在！必须是 2026-10-09 这样的真实日期")
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
def save_data():
    """把任务列表保存到文件 tasks.txt。
    每行格式：编号|标题|优先级|截止日期|状态
    参数：无
    返回：无
    """
    with open("tasks.txt", "w", encoding="utf-8") as f:
        #打开文件，覆盖原内容，用 UTF-8 编码，防止乱码，将打开的文件定义为f，方便后面使用
        for task in tasks:
            line = f"{task['id']}|{task['title']}|{task['priority']}|{task['deadline']}|{task['status']}"
            f.write(line + "\n")
    print("保存成功！数据已保存进文件。")
def load_data():
    """从文件 tasks.txt 读取上次保存的数据（程序启动时自动调用）。
    如果文件不存在（第一次运行），就不读，tasks 保持空列表。
    参数：无
    返回：无
    """
    try:
    #尝试读取之前task.txt文件里面的数据,因为是尝试所以就算失败了也不会报错
        with open("tasks.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()                #用来去掉line里面的换行符，打印的时候不会打出阿里
                if line == "":
                    continue
                parts = line.split("|")                 #列表格存储
                task = {
                    "id": int(parts[0]),
                    "title": parts[1],
                    "priority": parts[2],
                    "deadline": parts[3],
                    "status": parts[4]
                }
                tasks.append(task)              #将新的数据填写到tasks里面
        if len(tasks) > 0:
            print(f"已读取上次保存的 {len(tasks)} 个任务")
    except FileNotFoundError:                     #如果没有保存过，那就不会报错，直接退出
        pass
def show_info():
    if len(tasks) == 0:
        print("当前任务数量为0")
        return
    print("-------------------当前任务清单----------------------")
    for task in tasks:
        print(f"编号：{task['id']}")
        print(f"标题：{task['title']}")
        print(f"优先级：{task['priority']}")
        print(f"截止日期：{task['deadline']}")
        print(f"状态：{task['status']}")
        print("==============================================")
def task_mark():
    print()
    print("-----------------------任务标记------------------------")
    if len(tasks) == 0:
       print("暂无任务可标记！")
       return
    mark_id = input("请输入要标记完成的任务编号：").strip()
    if not mark_id.isdigit():
       print("请输入数字编号！")
       return
    mark_id = int(mark_id)
    found = False
    for task in tasks:
        if task["id"] == mark_id:
            task["status"] = "已完成"
            print(f"任务「{task['title']}」已标记为完成！")
            found = True
            break

    if not found:
        print(f"没有找到编号为 {mark_id} 的任务！")
def print_tasks_list(task_list):     #AI zuo de 辅助函数
    """用于统一格式化打印任务列表"""
    if len(task_list) == 0:
        print("暂无符合条件的任务。")
        return
    for task in task_list:
        print(f"编号: {task['id']} | 优先级: {task['priority']} | 截止日期: {task['deadline']} | 状态: {task['status']} | 标题: {task['title']}")
    print("-" * 60)
def search_task():
    print("====搜索与筛选====")
    print("1只看未完成")
    print("2只看已完成")
    print("3只看已逾期")
    print("4按关键字搜索")
    print("5按优先级排序查看")
    print("6按截止日期查看")
    print("7返回主菜单")

    choice=input("请输入选择")
    if choice == "1":
        result=[task for task in tasks if task["status"] == "未完成"] #遍历
        print("未完成的任务：")
        print_tasks_list(result)
    elif choice == "2":
        result=[task for task in tasks if task["status"]=="已完成"]
        print("只看已完成")
        print_tasks_list(result)
    elif choice == "3":
        # 逾期条件：未完成 且 截止日期小于今天
        result = [task for task in tasks if task["status"] == "未完成" and task["deadline"] < today_str]
        print("\n[只看已逾期]")
        print_tasks_list(result)
    elif choice == "4":
        keyword = input("请输入搜索关键字: ").strip()
        if keyword == "":
            print("关键字不能为空！")
            return
        result = [task for task in tasks if keyword in task["title"]]
        print(f"\n[关键字 '{keyword}' 的搜索结果]")
        print_tasks_list(result)
    elif choice == "5":       #问了AI
        # 优先级排序：高 -> 中 -> 低
        priority_order = {"高": 3, "中": 2, "低": 1}
        result = sorted(tasks, key=lambda x: priority_order.get(x["priority"], 0), reverse=True)
        print("\n[按优先级排序结果]")
        print_tasks_list(result)
    elif choice == "6":
        # 日期排序：字符串直接排序就是按时间先后
        result = sorted(tasks, key=lambda x: x["deadline"])
        print("\n[按截止日期排序结果]")
        print_tasks_list(result)
    elif choice == "7":
        return
    else:
        print("输入有误，请重新输入！")
main()


