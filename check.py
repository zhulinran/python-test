with open("test2.py", "r", encoding="utf-8") as f:
    code = f.read()

print("=" * 50)
print("       作业自动检查报告")
print("=" * 50)

checks = [
    ("1.添加任务-标题非空检查", 'title == ""'),
    ("1.添加任务-优先级校验", 'priority not in'),
    ("1.添加任务-日期格式校验", 'strptime'),
    ("1.添加任务-创建Task对象", 'Task('),
    ("2.查看全部-空列表提示", '当前任务数量为0'),
    ("2.查看全部-显示编号", 'task.id'),
    ("2.查看全部-显示优先级", 'task.priority'),
    ("2.查看全部-显示截止日期", 'task.deadline'),
    ("2.查看全部-显示状态", 'task.status'),
    ("2.查看全部-显示标题", 'task.title'),
    ("3.标记完成-输入编号", 'mark_id'),
    ("3.标记完成-校验数字", 'isdigit'),
    ("3.标记完成-改为已完成", 'mark_done'),
    ("4.删除任务-二次确认y/n", 'confirm == "y"'),
    ("4.删除任务-y/n循环重问", '请输入 y 或 n'),
    ("4.删除任务-删除后重新编号", 'tasks[j].id = j + 1'),
    ("4.删除任务-删除成功提示", '删除成功'),
    ("5.搜索-只看未完成", '未完成'),
    ("5.搜索-只看已完成", '已完成'),
    ("5.搜索-只看已逾期", 'deadline < today_str'),
    ("5.搜索-关键字搜索", 'keyword in task.title'),
    ("5.搜索-优先级排序", 'sorted'),
    ("5.搜索-日期排序", 'x.deadline'),
    ("7.保存-退出时自动保存", 'save_data()'),
    ("7.读取-启动时自动读取", 'load_data()'),
    ("8.导出-HTML文件", '<html>'),
    ("8.导出-文件名带日期", 'report_'),
    ("8.导出-完成率进度条", 'width:'),
    ("8.导出-逾期标红", 'color:red'),
    ("8.导出-明细表格", '<table'),
    ("9.健壮性-input加strip", '.strip()'),
    ("9.健壮性-数字校验isdigit", 'isdigit'),
    ("类-Task类定义", 'class Task'),
    ("类-mark_done方法", 'def mark_done'),
    ("类-show_info方法", 'def show_info'),
]

passed = 0
failed = 0

for name, keyword in checks:
    if keyword in code:
        print(f"  ✅ {name}")
        passed = passed + 1
    else:
        print(f"  ❌ {name}  ← 缺失！")
        failed = failed + 1

print("=" * 50)
print(f"通过：{passed} 项  缺失：{failed} 项")
if failed == 0:
    print("🎉 全部通过！")
else:
    print(f"⚠️  还有 {failed} 项缺失，快去补！")
print("=" * 50)