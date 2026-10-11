import datetime
import os
import cv2
import numpy as np

# 任务类
class Task:
    def __init__(self, title, priority, due_date, done):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.done = done

# 任务管理器
class TaskManager:
    def __init__(self):
        self.task_list = []
        self.load_data()

    # 加载本地文件
    def load_data(self):
        if not os.path.exists("tasks.txt"):
            return
        try:
            f = open("tasks.txt", "r", encoding="utf-8")
            lines = f.readlines()
            f.close()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                t = Task(parts[0], parts[1], parts[2], parts[3])
                self.task_list.append(t)
        except:
            print("读取任务文件失败")

    # 保存本地文件
    def save_data(self):
        f = open("tasks.txt", "w", encoding="utf-8")
        for t in self.task_list:
            line = f"{t.title}|{t.priority}|{t.due_date}|{t.done}\n"
            f.write(line)
        f.close()

    # 1. 添加任务
    def add_task(self):
        print("\n==== 添加任务 ====")
        title = input("任务标题：").strip()
        if title == "":
            print("错误：标题不能为空！")
            return
        prio = input("优先级(高/中/低)：").strip()
        if prio not in ["高", "中", "低"]:
            print("优先级只能填写：高、中、低")
            return
        due = input("截止日期(格式YYYY-MM-DD)：").strip()
        try:
            datetime.date.fromisoformat(due)
        except:
            print("日期格式不正确！")
            return
        new_task = Task(title, prio, due, "未完成")
        self.task_list.append(new_task)
        self.save_data()
        print("✅任务添加成功")

    # 2. 查看全部任务
    def show_all(self):
        print("\n==== 全部任务 ====")
        if len(self.task_list) == 0:
            print("任务清单为空")
            return
        for idx, t in enumerate(self.task_list):
            print(f"{idx+1}. 【{t.priority}】{t.title} |截止：{t.due_date} |状态：{t.done}")

    # 3. 标记完成
    def mark_done(self):
        self.show_all()
        if len(self.task_list) == 0:
            return
        s = input("\n输入要标记完成的任务编号：")
        if not s.isdigit():
            print("请输入数字！")
            return
        num = int(s)
        if num < 1 or num > len(self.task_list):
            print("编号不存在")
            return
        self.task_list[num-1].done = "已完成"
        self.save_data()
        print("✅标记为已完成")

    #4. 删除任务（二次确认）
    def del_task(self):
        self.show_all()
        if len(self.task_list) == 0:
            return
        s = input("\n输入要删除任务编号：")
        if not s.isdigit():
            print("请输入数字！")
            return
        num = int(s)
        if num <1 or num>len(self.task_list):
            print("编号不存在")
            return
        confirm = input(f"确认删除第{num}号任务？输入y确认：")
        if confirm == "y":
            del self.task_list[num-1]
            self.save_data()
            print("✅已删除")
        else:
            print("取消删除")

    #5.搜索筛选
    def filter_task(self):
        print("\n====筛选菜单====")
        print("1.只看未完成 2.只看已完成 3.只看已逾期")
        print("4.关键词搜索 5.按优先级排序 6.按截止日期排序")
        opt = input("选择：").strip()
        res = []
        today = str(datetime.date.today())
        if opt == "1":
            res = [t for t in self.task_list if t.done == "未完成"]
        elif opt == "2":
            res = [t for t in self.task_list if t.done == "已完成"]
        elif opt == "3":
            res = [t for t in self.task_list if t.done == "未完成" and t.due_date < today]
        elif opt == "4":
            keyword = input("输入关键词：")
            res = [t for t in self.task_list if keyword in t.title]
        elif opt == "5":
            prio_order = {"高":0,"中":1,"低":2}
            res = sorted(self.task_list, key=lambda x:prio_order[x.priority])
        elif opt == "6":
            res = sorted(self.task_list, key=lambda x:x.due_date)
        else:
            print("选项无效")
            return
        if len(res) == 0:
            print("无匹配任务")
            return
        for idx,t in enumerate(res):
            print(f"{idx+1}.【{t.priority}】{t.title} |截止：{t.due_date} |状态：{t.done}")

    #6.统计功能
    def show_stat(self):
        total = len(self.task_list)
        finished = len([t for t in self.task_list if t.done == "已完成"])
        unfinished = total - finished
        today = str(datetime.date.today())
        overdue = len([t for t in self.task_list if t.done == "未完成" and t.due_date < today])
        if total ==0:
            rate = 0.0
        else:
            rate = finished / total
        print("\n====任务统计====")
        print(f"任务总数：{total}")
        print(f"已完成：{finished}")
        print(f"未完成：{unfinished}")
        print(f"已逾期：{overdue}")
        print(f"完成率：{rate:.1%}")
        return total, finished, unfinished, overdue, rate

    #7自动保存：add/mark/del的时候已经调用save_data，满足要求

    #8导出HTML报告
    def export_html(self):
        total, finished, unfinished, overdue, rate = self.show_stat()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f"report_{datetime.date.today()}.html"
        rows = ""
        for idx,t in enumerate(self.task_list):
            rows += f"""
            <tr>
                <td>{idx+1}</td>
                <td>{t.priority}</td>
                <td>{t.due_date}</td>
                <td>{t.done}</td>
                <td>{t.title}</td>
            </tr>
            """
        html = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>任务报告</title>
<style>
body{{padding:30px; font-family:SimHei;}}
table{{border-collapse:collapse; width:80%;}}
td,th{{border:1px solid #333; padding:8px;}}
.bar{{width:300px;height:25px;border:1px solid black;}}
.inner{{height:100%;background:#4299e1;width:{rate*100}%;}}
</style>
</head>
<body>
<h1>任务清单报告</h1>
<p>生成时间：{now}</p>
<p>任务总数：{total}，已完成：{finished}，完成率{rate:.1%}</p>
<div class="bar"><div class="inner"></div></div>
<table>
<tr><th>编号</th><th>优先级</th><th>截止日期</th><th>状态</th><th>标题</th></tr>
{rows}
</table>
</body>
</html>
        """
        f = open(filename, "w", encoding="utf-8")
        f.write(html)
        f.close()
        print(f"\n✅HTML报告已导出：{filename}")

    # 9 OpenCV附加题：优先级条形图 高/中/低
    def draw_chart(self):
        high_cnt = 0
        mid_cnt = 0
        low_cnt = 0
        for task in self.task_list:
            if task.priority == "高":
                high_cnt += 1
            elif task.priority == "中":
                mid_cnt +=1
            elif task.priority == "低":
                low_cnt +=1
        data = [high_cnt, mid_cnt, low_cnt]
        labels = ["高优先级", "中优先级", "低优先级"]
        colors = [(0,0,255), (0,255,255), (0,255,0)]
        w, h =700,450
        img = np.ones((h,w,3), dtype=np.uint8)*255
        base_y =350
        bar_w =140
        gap =70
        maxv = max(data)
        if maxv ==0:
            maxv=1
        for i,num in enumerate(data):
            x1 = 60 + i*(bar_w+gap)
            x2 = x1 + bar_w
            bar_h = int(num/maxv*260)
            y1 = base_y - bar_h
            y2 = base_y
            cv2.rectangle(img, (x1,y1), (x2,y2), colors[i], -1)
            cv2.putText(img, str(num), (x1+50, y1-12), cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),2)
            cv2.putText(img, labels[i], (x1+25, base_y+35), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)
        cv2.putText(img, "任务优先级统计条形图", (200,45), cv2.FONT_HERSHEY_SIMPLEX,1.1,(0,0,0),2)
        timestr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        cv2.putText(img, f"生成时间：{timestr}", (180,90), cv2.FONT_HERSHEY_SIMPLEX,0.7,(40,40,40),2)
        cv2.imwrite("chart.png", img)
        print("\n✅条形图保存 chart.png")
        cv2.imshow("chart", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# 主菜单
def main():
    manager = TaskManager()
    while True:
        print("\n========任务管理系统========")
        print("1 添加任务")
        print("2 查看全部任务")
        print("3 标记任务完成")
        print("4 删除任务")
        print("5 搜索筛选任务")
        print("6 任务统计")
        print("7 数据保存")
        print("8 导出HTML报告")
        print("9 OpenCV生成优先级统计图")
        print("0 退出程序")
        op = input("请输入功能编号：").strip()
        if op == "1":
            manager.add_task()
        elif op == "2":
            manager.show_all()
        elif op == "3":
            manager.mark_done()
        elif op == "4":
            manager.del_task()
        elif op == "5":
            manager.filter_task()
        elif op == "6":
            manager.show_stat()
        elif op == "7":
            manager.save_data()
            print("✅手动保存完成")
        elif op == "8":
            manager.export_html()
        elif op == "9":
            manager.draw_chart()
        elif op == "0":
            manager.save_data()
            print("已保存数据，程序退出")
            break
        else:
            print("输入无效，请输入菜单里的数字！")

if __name__ == "__main__":
    main()
