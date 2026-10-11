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