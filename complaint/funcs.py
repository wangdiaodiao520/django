import os
import xlwt


def to_excel(complaint):
    if os.path.exists('投诉.xls'):
        os.remove('投诉.xls')
    else:
        pass

    # 创建一个文件对象
    file = xlwt.Workbook(encoding='utf8')
    # 创建一个sheet对象
    sheet = file.add_sheet('投诉',cell_overwrite_ok=True)

    # 设置文件头的样式,这个不是必须的可以根据自己的需求进行更改
    style_heading = xlwt.easyxf("""
                font:
                    name Arial,
                    colour_index white,
                    bold on,
                    height 0xA0;
                align:
                    wrap off,
                    vert center,
                    horiz center;
                pattern:
                    pattern solid,
                    fore-colour 0x19;
                borders:
                    left THIN,
                    right THIN,
                    top THIN,
                    bottom THIN;
                """)

    # 写入文件标题
    sheet.write(0, 0, '数据id', style_heading)
    sheet.write(0, 1, '网站id', style_heading)
    sheet.write(0, 2, '厂家', style_heading)
    sheet.write(0, 3, '车型', style_heading)
    sheet.write(0, 4, '年款', style_heading)
    sheet.write(0, 5, '简述', style_heading)
    sheet.write(0, 6, '问题', style_heading)
    sheet.write(0, 7, '投诉时间', style_heading)
    sheet.write(0, 8, '描述', style_heading)

    # 写入数据
    data_row = 1
    for i in complaint:
        sheet.write(data_row, 0, i.id)
        sheet.write(data_row, 1, i.ts_id)
        sheet.write(data_row, 2, i.cj)
        sheet.write(data_row, 3, i.cx)
        sheet.write(data_row, 4, i.nk)
        sheet.write(data_row, 5, i.js)
        sheet.write(data_row, 6, i.wt)
        sheet.write(data_row, 7, i.time)
        sheet.write(data_row, 8, i.ms)
        data_row = data_row + 1
    file.save('投诉.xls')