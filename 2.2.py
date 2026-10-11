from datetime import datetime       #引入datetime模块来帮助判断日期格式是否规范

# ========== Task 类 ==========
class Task:
    """一条任务。
    属性：id, title, priority, deadline, status
    方法：mark_done(), show_info()
    """
    def __init__(self, task_id, title, priority, deadline):
        self.id = task_id               # 编号
        self.title = title              # 标题
        self.priority = priority        # 优先级（高/中/低）
        self.deadline = deadline        # 截止日期
        self.status = "未完成"          # 状态

    def mark_done(self):
        """把任务标记为已完成"""
        self.status = "已完成"

    def show_info(self):
        """打印任务信息"""
        print(f"编号：{self.id}")
        print(f"标题：{self.title}")
        print(f"优先级：{self.priority}")
        print(f"截止日期：{self.deadline}")
        print(f"状态：{self.status}")

tasks = []     #任务列表，用来收集任务和排列任务
today_str = datetime.now().strftime("%Y-%m-%d")    # 今天的日期，用来判断逾期

def show_menu():
    print("----------------控制台菜单----------------")
    print("1添加任务")
    print("2查看全部")
    print("3标记完成")
    print("4删除任务")
    print("5搜索与筛选")
    print("6统计")
    print("7导出报告")
    print("8退出系统")
    print("=========================================")

def main():
    load_data()                                                       #用来读取上一次程序保存的数据
    while True:
        show_menu()
        choice = input("请输入您的操作编号：").strip()
        if choice == "8":
            save_data()
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
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            export_html()
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
    task = Task(task_id, title, priority, deadline)                 #创建Task对象
    tasks.append(task)                                #将新的任务储存到tasks字典的最末端
    print(f"添加成功！任务信息如下：")
    task.show_info()                                   #调用类里的show_info方法打印信息

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
        print(f"编号：{task.id} | 标题：{task.title}")
    task_id = input("请输入您想要删除任务的编号：").strip()
    if not task_id.isdigit():                         #这玩意是用来检验是否全是数字
        print("请输入数字编号！！！")
        return
    task_id = int(task_id)
    found = False
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            while True:
                confirm = input(f"确定要删除任务「{tasks[i].title}」吗？(y/n)：").strip().lower()
                #lower可以使输入进来的全变成小写，这样输入大写的Y,N也没事
                if confirm == "y":
                    del tasks[i]
                    for j in range(len(tasks)):
                        tasks[j].id = j + 1
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
            line = f"{task.id}|{task.title}|{task.priority}|{task.deadline}|{task.status}"
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
                task = Task(int(parts[0]), parts[1], parts[2], parts[3])
                task.status = parts[4]
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
        task.show_info()
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
        if task.id == mark_id:
            task.mark_done()
            print(f"任务「{task.title}」已标记为完成！")
            found = True
            break

    if not found:
        print(f"没有找到编号为 {mark_id} 的任务！")
def export_html():
    # 生成任务的html报告，保存到当前文件夹
    html_lines = []
    html_lines.append("<html>")
    html_lines.append("<head><meta charset='utf-8'><title>任务清单报告</title></head>")
    html_lines.append("<body>")
    html_lines.append("<h2>任务汇总表</h2>")

    # 统计数据：总数、已完成数、完成率
    total = len(tasks)
    if total == 0:                                   #空列表判断
        print("暂无任务，无法导出报告！")
        return
    done_count = 0
    for task in tasks:
        if task.status == "已完成":
            done_count = done_count + 1
    rate = done_count / total * 100

    html_lines.append(f"<p>生成日期：{today_str}</p>")
    html_lines.append(f"<p>任务总数：{total}　已完成：{done_count}　完成率：{rate:.1f}%</p>")
    # 完成率进度条
    html_lines.append(f'<div style="width:300px;background:#eee;border:1px solid #ccc;">')
    html_lines.append(f'<div style="width:{rate:.1f}%;background:#4caf50;height:20px;"></div>')
    html_lines.append(f"</div>")

    html_lines.append("<table border='1' cellpadding='5'>")
    html_lines.append("<tr><th>编号</th><th>优先级</th><th>截止日期</th><th>状态</th><th>任务名称</th></tr>")

    for task in tasks:
        # task.status 是字符串，"已完成"代表任务做完了，"未完成"代表还没做完
        # 如果是未完成且截止日期早于今天，说明逾期了，标红显示
        if task.status == "未完成" and task.deadline < today_str:
            row_style = 'style="color:red;"'
        else:
            row_style = ""
        html_lines.append(
            f"<tr {row_style}><td>{task.id}</td><td>{task.priority}</td>"
            f"<td>{task.deadline}</td><td>{task.status}</td><td>{task.title}</td></tr>"
        )

    html_lines.append("</table>")
    html_lines.append("</body></html>")

    # 把全部内容拼在一起，写入文件
    save_name = f"report_{today_str}.html"
    full_html = "\n".join(html_lines)
    with open(save_name, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"报告导出成功，文件名：{save_name}")
def print_tasks_list(task_list):
    """用于统一格式化打印任务列表"""
    if len(task_list) == 0:
        print("暂无符合条件的任务。")
        return
    for task in task_list:
        print(f"编号：{task.id} | 优先级：{task.priority} | 截止日期：{task.deadline} | 状态：{task.status} | 标题：{task.title}")

def search_task():
    print("===搜索与筛选===")
    print("1只看未完成")
    print("2只看已完成")
    print("3只看已逾期")
    print("4按关键字搜索")
    print("5按优先级排序查看")
    print("6按截止日期排序查看")
    print("7返回主菜单")

    choice = input("请输入选择：")

    if choice == "1":
        result = [task for task in tasks if task.status == "未完成"]  #遍历
        print_tasks_list(result)
    elif choice == "2":
        result = [task for task in tasks if task.status == "已完成"]
        print_tasks_list(result)
    elif choice == "3":
        # 逾期条件：未完成 且 截止日期小于今天
        result = [task for task in tasks if task.status == "未完成" and task.deadline < today_str]
        print("\n[只看已逾期]")
        print_tasks_list(result)
    elif choice == "4":
        keyword = input("请输入搜索关键字：").strip()
        if keyword == "":
            print("关键字不能为空！")
            return
        result = [task for task in tasks if keyword in task.title]
        print(f"\n[关键字 '{keyword}' 的搜索结果]")
        print_tasks_list(result)
    elif choice == "5":
        # 优先级排序：高 -> 中 -> 低
        priority_order = {"高": 3, "中": 2, "低": 1}
        result = sorted(tasks, key=lambda x: priority_order.get(x.priority, 0), reverse=True)
        print("\n[按优先级排序结果]")
        print_tasks_list(result)
    elif choice == "6":
        # 日期排序：字符串直接排序就是按时间先后
        result = sorted(tasks, key=lambda x: x.deadline)
        print("\n[按截止日期排序结果]")
        print_tasks_list(result)
    elif choice == "7":
        return
    else:
        print("输入有误，请重新输入！")

def show_statistics():
    print("\n===== 任务统计 =====")
    total = len(tasks)

    if total == 0:
        print("当前任务数为 0，暂无统计信息。")
        return

    today_str = datetime.now().strftime("%Y-%m-%d")

    # 使用列表推导式统计
    completed = sum(1 for task in tasks if task.status== "已完成")
    uncompleted = total - completed
    overdue = sum(1 for task in tasks if task.status == "未完成" and task.deadline < today_str)

    # 计算完成率
    completion_rate = (completed / total) * 100

    print(f"任务总数: {total}")
    print(f"已完成数: {completed}")
    print(f"未完成数: {uncompleted}")
    print(f"已逾期数: {overdue}")
    print(f"完成率: {completion_rate:.2f}%")
    print("=" * 22)
main()