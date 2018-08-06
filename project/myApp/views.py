from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .models import Grades, Students


# Create your views here.
def Index(request):
    return HttpResponse("Hello Python!!!!")

def Index1(request):
    return HttpResponseRedirect('/sunck/')

def detail(request, num):
    return HttpResponse("detail-%s" % num)


def grades(request):
    # 从模型中获取数据
    gradesList = Grades.objects.all()
    # 将数据返回至grades.html
    return render(request, "myApp/grades.html", {"grades": gradesList})


def students(request):
    # 从模型中获取数据
    studentsList = Students.objects.all()
    # 将数据返回至grades.html
    return render(request, "myApp/students.html", {"students": studentsList})


# 查看属性
def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)

    return HttpResponse('attribles')


# 用get获取网址中的值
def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')

    return HttpResponse(a + b + c)


def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    b = request.GET.get('b')
    c = request.GET.get('c')

    return HttpResponse(a1 + a2 + b + c)


# 用post获取网址中值
# 显示注册界面
def showregistered(request):
    return render(request, 'myApp/registered.html')


def registered(request):
    name = request.POST.get("name")
    gener = request.POST.get("gener")
    age = request.POST.get("age")
    hobby = request.POST.get("hobby")
    print(name + gener + age + hobby)
    return HttpResponse("post成功")


# 测试response的属性
def response(request):
    res = HttpResponse()
    res.content = b'good'
    print(res.content)
    print(res.content - type)
    print(res.charset)
    print(res.status_code)

    return res

# 测试cookie
def cookieTest(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write('<h1>' + cookie['name'] + '</h1>')
    # cookie = res.set_cookie('name','zcs')
    return res

# 测试重定向
def redirect1(request):
    #return HttpResponseRedirect('/sunck/redirect2/')
    return redirect('/sunck/redirect2/')

def redirect2(request):
    return HttpResponse('重定向成功')
