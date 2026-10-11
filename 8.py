def export_html(task_list, save_name="task_report.html"):
    # 生成任务的html报告，保存到当前文件夹
    html_lines = []
    html_lines.append("<html>")
    html_lines.append("<head><meta charset='utf-8'><title>任务清单报告</title></head>")
    html_lines.append("<body>")
    html_lines.append("<h2>任务汇总表</h2>")
    html_lines.append("<table border='1'>")
    html_lines.append("<tr><th>任务名称</th><th>截止时间</th><th>状态</th></tr>")

    for item in task_list:
        task_name = item["name"]
        deadline = item["deadline"]
        # item["done"] 是布尔值，True代表任务完成，False代表还没做完
        if item["done"]:
            status_text = "已完成"
        else:
            status_text = "未完成"
        html_lines.append(f"<tr><td>{task_name}</td><td>{deadline}</td><td>{status_text}</td></tr>")

    html_lines.append("</table>")
    html_lines.append("</body></html>")

    # 把全部内容拼在一起，写入文件
    full_html = "\n".join(html_lines)
    with open(save_name, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"报告导出成功，文件名：{save_name}")
