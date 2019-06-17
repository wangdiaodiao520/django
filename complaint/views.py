from django.shortcuts import render,redirect,render_to_response
from .models import UserForm,User,Complaint
import datetime
from .echarts import *
from .funcs import *
from django.http import StreamingHttpResponse


# Create your views here.
def index(request):
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            user_name = login_form.cleaned_data['user_name']
            user_password = login_form.cleaned_data['user_password']
            '''添加验证'''
            try:
                user = User.objects.get(user_name = user_name)
                if user.user_password == user_password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.user_name
                    return redirect('/index/')
                else:
                    message = "密码错误"
            except:
                message = "用户不存在"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html',locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")

    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")


def complaints(request):
    cj = str(request.GET.get('cj'))
    cx = str(request.GET.get('cx'))
    bw = str(request.GET.get('bw'))
    start = str(request.GET.get('start'))
    end = str(request.GET.get('end'))
    ly = str(request.GET.get('ly'))
    if not any([cj, cx, bw, start, end, ly]):
        start = end = (datetime.date.today() + datetime.timedelta(-1)).strftime("%Y-%m-%d")
    else:
        if start == '':
            start = datetime.datetime.strptime('1990-01-01', '%Y-%m-%d')
        if end == '':
            end = datetime.datetime.strptime('2099-12-31', '%Y-%m-%d')
    if ly == '车质网':
        ly = 'czw'
    elif ly == '汽车投诉网':
        ly = 'QT'
    else:
        ly = ''
    global tss
    tss = None
    complaint = Complaint.objects.filter(cj__icontains=cj, cx__icontains=cx, wt__icontains=bw, ts_id__icontains=ly,time__range=[start, end]).order_by('-time')
    tss = complaint
    chart ={}
    if cj =='' and cx == '':
        chart['cj_bar'] = cj_to_bar(complaint).render_embed()
        chart['cx_pie'] = cx_to_pie(complaint).render_embed()
    elif cj !='' and cx == '':
        chart['cx_pie'] =cx_to_pie(complaint).render_embed()
    else:pass
    chart['wt_bar'] = wt_to_bar(complaint).render_embed()
    chart['bw_pie'] = bw_to_pie(complaint).render_embed()
    chart['nk_pie'] = nk_to_pie(complaint).render_embed()
    return render_to_response('login/complaint.html', chart)


def download(request):
    global tss
    to_excel(tss)
    file_name = '投诉.xls'
    def file_iterator(file_name, chunk_size=512):  # 用于形成二进制数据
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    response = StreamingHttpResponse(file_iterator(file_name))  # 这里创建返回
    response['Content-Type'] = 'application/vnd.ms-excel'  # 注意格式
    response['Content-Disposition'] = 'attachment;filename="投诉.xls"'  # 注意filename 这个是下载后的名字
    return response



















