from  pyecharts import Bar,Pie


def wt_to_bar(complaints):
    data = {}
    attr = []
    value = []
    for i in complaints:
        for i in i.wt.split(','):
            if i in data.keys():
                data[i] += 1
            else:
                data[i] = 1
    for k in sorted(data,key=data.__getitem__,reverse=True):
        attr.append(k)
        value.append(data[k])
    bar = Bar('投诉问题分布图', width=1300, height=300)
    bar.add('', attr, value, is_datazoom_show=True, is_label_show=True)
    return bar

def bw_to_pie(complaints):
    data = {}
    for i in complaints:
        for i in i.wt.split(','):
            wt = i.split('#')
            if wt[0] in data.keys():
                data[wt[0]] += 1
            else:
                data[wt[0]] = 1
    attr = list(data.keys())
    value = list(data.values())

    pie =  Pie('投诉部位分布图',width=1300)
    pie.add('',attr,value,is_legend_show=False, is_label_show=True)
    return  pie

def nk_to_pie(complaints):
    data = {}
    for i in complaints:
        if i.nk[:4].isdigit():
            nk = i.nk[:4]
            if nk in data.keys():
                data[nk] += 1
            else:
                data[nk] = 1
        else:pass
    attr = list(data.keys())
    value = list(data.values())
    pie = Pie('投诉年款分布图', width=1300)
    pie.add('', attr, value, is_label_show=True)
    return pie

def cj_to_bar(complaints):
    data = {}
    attr = []
    value = []
    for i in complaints:
        cj = i.cj
        if cj in data.keys():
            data[cj] += 1
        else:
            data[cj] = 1
    for k in sorted(data,key=data.__getitem__,reverse=True):
        attr.append(k)
        value.append(data[k])
    bar = Bar('投诉厂家分布图', width=1300, height=300)
    bar.add('', attr, value, is_datazoom_show=True, is_label_show=True)
    return bar

def cx_to_pie(complaints):
    data = {}
    attr = []
    value = []
    for i in complaints:
        cx = i.cx
        if cx in data.keys():
            data[cx] += 1
        else:
            data[cx] = 1
    for k in sorted(data,key=data.__getitem__,reverse=True):
        attr.append(k)
        value.append(data[k])
    pie = Pie('投诉车型分布图', width=1300)
    if len(attr) > 15:
        pie.add('所有车型', attr, value, center=[30, 50],is_legend_show=False)
        pie.add('前十车型', attr[:10], value[:10], center=[70, 50],is_legend_show=False,is_label_show=True)
    else:
        pie.add('所有车型', attr, value, is_label_show=True)
    return pie



















