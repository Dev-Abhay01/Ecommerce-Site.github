from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


# Create your views here.
def home(request):

    cdata=category.objects.all().order_by('-id')[0:6]
    cursor=connection.cursor()
    cursor.execute("select b.*,u.* from user_blogdetail b, user_signup u where b.authorid=u.email order by b.blogdate desc")
    return render(request,'user/index.html',{"data":cdata,"bdetail":blogdetail})

def about(request):
    return render(request,'user/about.html')
# def about(request):
#     return render(request,'user/about.html')
def contactus(request):
    status=False
    if request.method=='POST':
        Name=request.POST.get("name","")
        Contact=request.POST.get("mobile","")
        Email=request.POST.get("email","")
        Message=request.POST.get("msg","")
        x=contact(name=Name,email=Email,contact=Contact,message=Message)
        x.save()
        status=True
       # return HttpResponse("<script>alert('Thanks for enquiry..');windows.location.href='/user/contactus/';</script>")
    return render(request,'user/contactus.html',{'S':status})

def services(request):
    return render(request,'user/services.html')

def createblog (request):
    status=False
    if request.session.get('user'):
        cdata = category.objects.all()
        if request.method=='POST':
            Authorid=request.session.get('user')
            Category=request.POST.get('category')
            Btopic=request.POST.get('title')
            Description=request.POST.get('description')
            Attach=request.FILES['attachment']
            Thumbnail=request.FILES['thumbnail']
            res=blogdetail(authorid=Authorid,blogcategory=Category,btitle=Btopic,bdescription=Description,battachment=Attach,bthumbnail=Thumbnail,blogdate=datetime.datetime.now())
            res.save()
            status = True
        return render(request,'user/createblog.html',{"category":cdata,'R':status})
    else:
     return HttpResponse("<script>alert('Plese login first to add blogs..');window.location.href='/user/signin/';</script>")

def myblog (request):
    if request.session.get('user'):
        id=request.session.get('user')
        blogdata=blogdetail.objects.filter(authorid=id).order_by('-blogdate')
        return render(request,'user/myblog.html',{"bdata":blogdata})
    else:
     return HttpResponse("<script>alert('Plese login first to see blog list..');window.location.href='/user/signin/';</script>")


def signin(request):
    if request.method=='POST':
        uname=request.POST.get('mail')
        upass=request.POST.get('pass')
        checkuser=signup.objects.filter(email=uname,password=upass)
        #print(checkuser)
        if(checkuser):
            request.session["user"]=uname
            return HttpResponse("<script>alert('logged in successfully..');window.location.href='/user/home/';</script>")
        else:
            return HttpResponse("<script>alert('user id or password incorrect..');window.location.href='/user/signin/';</script>")

    return render(request,'user/signin.html')

def logout(request):
    del request.session['user']
    return HttpResponse("<script>window.location.href='/user/home/';</script>")

def register(request):
    if request.method=='POST':
        Name=request.POST.get("name","")
        dob=request.POST.get("DOB","")
        Gender=request.POST.get("Gender","")
        Mobile=request.POST.get("mobile","")
        Email=request.POST.get("email","")
        Password=request.POST.get("password","")
        Profession=request.POST.get("profession","")
        Working=request.POST.get("working","")
        Picture=request.FILES['fu']
        signup(name=Name,DOB=dob,gender=Gender,Mobile=Mobile,email=Email,password=Password,profession=Profession,working=Working,profile_picture=Picture).save()
        return HttpResponse("<script>alert('you are Registered successfully..');window.location.href='/user/signin/';</script>")

    return render(request,'user/signup.html')

def latestblog (request):
    cursor=connection.cursor()
    if(request.GET.get('id') is None):
        cursor.execute("select b.*,u.* from user_blogdetail b, user_signup u where b.authorid=u.email order by b.blogdate desc")
    else:
        id=request.GET.get('id')
        cursor.execute("select b.*,u.* from user_blogdetail b, user_signup u where b.authorid=u.email and b.blogcategory='"+id+"' order by b.blogdate desc limit 0,6")
    blogdetail=cursor.fetchall()
    cdata=category.objects.all().order_by('id')
    return render(request,'user/latestblog.html',{"bdetail":blogdetail,"data":cdata})
def myprofile (request):
    if request.session.get('user'):
        id=request.session.get('user')
        userdata=signup.objects.filter(email=id)
        return render(request,'user/myprofile.html',{"udata":userdata})
    else:
        return HttpResponse("<script>alert('please login first to see your profile..');window.location.href='/user/signin/';</script>")


def editprofile (request):
    return render(request,'user/editprofile.html')


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#
#         central_widget.setContextMenuPolicy(Qt.NoContextMenu)
#
# def main():
#     app = QApplication(sys.argv)
#     mainWindow = MainWindow()
#     mainWindow.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()
