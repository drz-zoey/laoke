import sys
import re
import openpyxl

# 打开excel表格，新建或打开已有表格
workbook = openpyxl.Workbook()
worksheet = workbook.active

input_file = sys.argv[1]
output_file = sys.argv[2] + "\\result.xlsx"

# 逐行读取文本文件
with open(input_file, 'r' , encoding='utf-8') as f:
    line_num = 2
    undo_num = 3
    worksheet.cell(row=line_num, column=2).value = '品牌'
    worksheet.cell(row=line_num, column=3).value = '商品'
    worksheet.cell(row=line_num, column=4).value = '价格（元）'
    worksheet.cell(row=line_num, column=5).value = '来源'
    worksheet.cell(row=line_num, column=7).value = '待处理'
    line_num = line_num+1

    for line in f:
        # 提取每行末尾的数字，作为价格
        price_match = re.search(r"\d+$", line.strip())
        if price_match:
            price = price_match.group()
            name = line[:price_match.start()].strip()
        else:
            price = ""
            name = line.strip()

        # 提取出现的品牌名称
        brand_match = re.search(r"(兰蔻|雅诗兰黛|圣罗兰|YSL|cpb|海蓝之谜|娇韵诗|阿玛尼|赫莲娜|科颜氏|gucci|倩碧|黛珂|资生堂|迪奥|莱珀妮|HR|娇兰|sk2|植村秀|TF|NARS|MAC|魅可|whoo|雅萌|ahc|飞利浦|百瑞德|悦薇)", line)
        if brand_match:
            brand = brand_match.group()
        else:
            brand = ""

        # 提取括号内的内容，作为来源地
        source_match = re.search(r"\（(.*?)\）", line)
        if source_match:
            source = source_match.group(1)
        else:
            source = ""

        print("brand:"+brand)
        print("name:"+name)
        print("price:"+price)
        print("source:"+source)
        
        # 将提取到的信息及匹配失败项写入excel表格
        if price or brand or source:
            worksheet.cell(line_num, 2, brand)
            worksheet.cell(line_num, 3, name)
            worksheet.cell(line_num, 4, price)
            worksheet.cell(line_num, 5, source)
            line_num = line_num + 1
        else:
            undo = line.strip()
            if undo:
                worksheet.cell(undo_num, 7, line.strip())
                undo_num = undo_num + 1

# 保存excel表格
workbook.save(output_file)