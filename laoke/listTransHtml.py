import re

# 正则表达式：匹配行末数字
price_pattern = re.compile(r'\d+[.]?\d*$')

# 正则表达式：匹配品牌
brand_pattern = re.compile(r'兰蔻|卡诗|雅诗兰黛|卡地亚|玫珂菲|圣罗兰|蒂佳婷|cpb肌肤之钥|海蓝之谜|娇韵诗|阿玛尼|赫莲娜|科颜氏|Gucci|倩碧|黛珂|资生堂|馥蕾诗|欧莱雅|迪奥|莱珀妮|赫莲娜|娇兰|SK-II|植村秀|Tom Ford|NARS|MAC|魅可|whoo后|雅萌|ahc|飞利浦|百瑞德|兰芝|香奈儿|银座|菲拉格慕|衰败城市|伊菲丹|芭比布朗|祖玛龙|希思黎|碧欧泉|欧舒丹|修丽可|爱马仕|蔻依|祖玛珑|梅森马吉拉')

#根据单品名称匹配品牌
brand_match_skii_pattern = re.compile(r'(SK2|sk2|skii|sk-ii|skll|晶莹露|眼面套|神灯套|小灯泡|神仙水|大红瓶|前男友|甄选三件套|增选3件套)')
brand_match_ysld_pattern = re.compile(r'(增量五件套|抗衰|红石榴|小棕瓶|蓝光眼霜|抗蓝光|眼绷带|白金眼霜|白金粉底液|沁水|dw|原生液|樱花水|智妍|抗衰老|黑松露|白金面霜)')
brand_match_hlzm_pattern = re.compile(r'(LAMER|Lamer|lamer|绿眼霜|精粹水|精粹乳|精萃乳|海南之谜|舒缓喷雾|浓缩精华|经典面霜)')
brand_match_zst_pattern = re.compile(r'(安耐晒|安热沙|蓝胖子|红腰子|悦薇|百优|百忧)')
brand_match_cpb_pattern = re.compile(r'(cpb|肌肤之钥|CPB|Cpb|长管隔离)')
brand_match_whoo_pattern = re.compile(r'(whoo|天气丹|天率丹|拱辰享|津率享)')
brand_match_tf_pattern = re.compile(r'(TF|Tf|tf|tom ford|Tom Ford|TOM FORD|乌木|乌木沉香)')
brand_match_xsl_pattern = re.compile(r'(希思黎|sisley|Sisley|全能乳)')
brand_match_xlk_pattern = re.compile(r'(修丽可|色修|紫米精华|CE精华|SCF抗氧)')
brand_match_ahc_pattern = re.compile(r'(ahc|Ahc|AHC|黄金面膜)')
brand_match_nars_pattern = re.compile(r'(nars|Nars|纳斯|超方瓶|大白饼)')
brand_match_msmjl_pattern = re.compile(r'(马吉拉|梅森马吉拉|慵懒周末)')
brand_match_lk_pattern = re.compile(r'(小白管|菁纯|箐纯|小黑瓶|大眼精华|发光眼霜|肌底液|雪花霜|粉水|极光|持妆|是我|三件套带水|带水三件套|小蛮腰)')
brand_match_kys_pattern = re.compile(r'(金盏花|宝宝霜|高保湿|白泥|紫波A面霜|爱海南三件套|淡斑精华)')
brand_match_qb_pattern = re.compile(r'(倩碧|紫光|镭射)')
brand_match_amn_pattern = re.compile(r'(玉龙茶香|黑曜石|黑钥匙|myway|MY WAY|My Way|my way|自我无界|大师|权力)')
brand_match_ysl_pattern = re.compile(r'(圣罗兰|YSL|ysl|Ysl|yls|夜皇后|藏金|粉气垫|皮气垫|小金条|小黑条|小粉条)')
brand_match_gucci_pattern = re.compile(r'(Gucci|gucci|古驰)')
brand_match_hr_pattern = re.compile(r'(Hr|HR|赫莲娜|黑绷带|白绷带|绿宝瓶|黑白绷带|小针管|小露珠)')
brand_match_sbcs_pattern = re.compile(r'(衰败城市|牛郎|URBAN DECAY|Urban Decay|urban decay)')
brand_match_ky_pattern = re.compile(r'(寇依|蔻依|chole|chloe|Chloe|CHLOE|北国雪松|木兰诗语)')
brand_match_zml_pattern = re.compile(r'(祖玛珑|祖马龙|蓝风铃)')
brand_match_phlg_pattern = re.compile(r'(PENHALIGON\'S|潘海利根|兽首)')
brand_match_pola_pattern = re.compile(r'(POLA|pola|Pola|宝丽|黑BA|黑ba|黑Ba)')
brand_match_zcx_pattern = re.compile(r'(琥珀|琥珀卸妆油|柚子卸妆油|绿茶卸妆油)')
brand_match_ams_pattern = re.compile(r'(爱马仕|大地)')
brand_match_xne_pattern = re.compile(r'(香奈儿|channel|蔚蓝|山茶花洁面|山茶花|嘉伯丽尔|黄邂逅|粉邂逅|绿邂逅)')
brand_match_jys_pattern = re.compile(r'(娇韵诗|双萃|弹簧水)')
brand_match_lyw_pattern = re.compile(r'(罗意威|Loewe|loewe)')
brand_match_boq_pattern = re.compile(r'(碧欧泉|水动力)')
brand_match_lbn_pattern = re.compile(r'(莱伯妮|莱珀妮|LP|La Prairie)')


# 正则表达式：匹配来源地
source_pattern = re.compile(r'\((.*?)\)')

path = "C:\\Users\\John\\Desktop\\laoke\\laoke\\example.txt"
#path = "F:\Material\互助\code\laoke\example.txt"

# 读取文本，进行数据提取和匹配
with open(path, 'r', encoding='utf-8') as f:
    # 读取文件内容并去除空白符
    lines = [line.strip() for line in f.readlines()]

# 定义数据表格
table_data = []

# 遍历每行文本，进行正则匹配
for line in lines:
    # 匹配价格
    price_match = re.findall(price_pattern, line)
    if price_match:
        # 提取价格
        price = float(price_match[-1])
        
        # 提取商品名称，即行中除最后一个数字和空白符的部分
        name = re.sub(price_pattern, '', line).strip()
        
        # 匹配品牌
        brand_match = re.findall(brand_pattern, line)

        brand_match_skii = re.findall(brand_match_skii_pattern, line)
        brand_match_ysld = re.findall(brand_match_ysld_pattern, line)
        brand_match_hlzm = re.findall(brand_match_hlzm_pattern, line)
        brand_match_zst = re.findall(brand_match_zst_pattern, line)
        brand_match_cpb = re.findall(brand_match_cpb_pattern, line)
        brand_match_whoo = re.findall(brand_match_whoo_pattern, line)
        brand_match_tf = re.findall(brand_match_tf_pattern, line)
        brand_match_xsl = re.findall(brand_match_xsl_pattern, line)
        brand_match_xlk = re.findall(brand_match_xlk_pattern, line)
        brand_match_ahc = re.findall(brand_match_ahc_pattern, line)
        brand_match_nars = re.findall(brand_match_nars_pattern, line)
        brand_match_msmjl = re.findall(brand_match_msmjl_pattern, line)
        brand_match_lk = re.findall(brand_match_lk_pattern, line)
        brand_match_kys = re.findall(brand_match_kys_pattern, line)
        brand_match_qb = re.findall(brand_match_qb_pattern, line)
        brand_match_amn = re.findall(brand_match_amn_pattern, line)
        brand_match_ysl = re.findall(brand_match_ysl_pattern, line)
        brand_match_gucci = re.findall(brand_match_gucci_pattern, line)
        brand_match_hr = re.findall(brand_match_hr_pattern, line)
        brand_match_sbcs = re.findall(brand_match_sbcs_pattern, line)
        brand_match_ky = re.findall(brand_match_ky_pattern, line)
        brand_match_zml = re.findall(brand_match_zml_pattern, line)
        brand_match_phlg = re.findall(brand_match_phlg_pattern, line)
        brand_match_pola = re.findall(brand_match_pola_pattern, line)
        brand_match_zcx = re.findall(brand_match_zcx_pattern, line)
        brand_match_ams = re.findall(brand_match_ams_pattern, line)
        brand_match_xne = re.findall(brand_match_xne_pattern, line)
        brand_match_jys = re.findall(brand_match_jys_pattern, line)
        brand_match_lyw = re.findall(brand_match_lyw_pattern, line)
        brand_match_boq = re.findall(brand_match_boq_pattern, line)
        brand_match_lbn = re.findall(brand_match_lbn_pattern, line)

        if brand_match:
            brand = brand_match[0]
        elif brand_match_skii:
            brand = "SK-II"
        elif brand_match_ysld:
            brand = "雅诗兰黛"
        elif brand_match_hlzm:
            brand = "海蓝之谜"
        elif brand_match_zst:
            brand = "资生堂"
        elif brand_match_cpb:
            brand = "cpb肌肤之钥"
        elif brand_match_whoo:
            brand = "whoo后"
        elif brand_match_tf:
            brand = "Tom Ford"
        elif brand_match_xsl:
            brand = "Sisley希思黎"
        elif brand_match_xlk:
            brand = "修丽可"
        elif brand_match_ahc:
            brand = "AHC爱和纯"
        elif brand_match_nars:
            brand = "NARS"
        elif brand_match_msmjl:
            brand = "梅森马吉拉"
        elif brand_match_lk:
            brand = "兰蔻"
        elif brand_match_kys:
            brand = "科颜氏"
        elif brand_match_qb:
            brand = "倩碧"
        elif brand_match_amn:
            brand = "Amani阿玛尼"
        elif brand_match_ysl:
            brand = "Ysl圣罗兰"
        elif brand_match_gucci:
            brand = "Gucci"
        elif brand_match_hr:
            brand = "赫莲娜"
        elif brand_match_ky:
            brand = "chloe蔻依"
        elif brand_match_zml:
            brand = "祖玛珑"
        elif brand_match_phlg:
            brand = "潘海利根"
        elif brand_match_pola:
            brand = "POLA 宝丽"
        elif brand_match_zcx:
            brand = "植村秀"
        elif brand_match_ams:
            brand = "爱马仕"
        elif brand_match_xne:
            brand = "香奈儿"
        elif brand_match_jys:
            brand = "娇韵诗"
        elif brand_match_lyw:
            brand = "罗意威"
        elif brand_match_boq:
            brand = "碧欧泉"
        elif brand_match_lbn:
            brand = "莱铂妮"
        else:
            brand = ""

        # 匹配来源地
        source_match = re.findall(source_pattern, line)
        if source_match:
            # 提取来源地
            source = source_match[0]
        else:
            source = ''
            
        # 将提取到的信息添加至数据表格
        table_data.append([name, price, brand, source])
    else:
        # 将匹配失败的行加入失败项数据表格
        table_data.append([line, '', '', ''])

# 将数据表格转换为HTML表格
table_html = "<table><tr><th>商品名称</th><th>价格</th><th>品牌</th><th>来源地</th></tr>"
for row in table_data:
    table_html += "<tr>"
    for col in row:
        table_html += "<td>" + str(col) + "</td>"
    table_html += "</tr>"
table_html += "</table>"

# 将HTML表格输出为HTML文件
with open("table.html", 'w', encoding='utf-8') as f:
    f.write(table_html)