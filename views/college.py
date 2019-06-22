from django.contrib import messages
from django.views import View
from onlineapp.models import *
from django.shortcuts import *
from onlineapp.forms import *
from django.urls import resolve
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin



def logout_user(request):
    logout(request)
    return redirect('login_html')


class CollegeView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        user_permissions=request.user.get_all_permissions()
        if(kwargs):
            obj = College.objects.filter(id=kwargs['collegeid']).values('student__name', 'student__mocktest1__total','student__email','student__id')
            collegename = College.objects.filter(id=kwargs['collegeid']).values('name')
            return render(request, template_name="onlineapp/student_info.html",context={'studs': obj, 'Title': '{0}'.format(collegename[0]['name']),'collegeid':kwargs['collegeid'],'user_permissions':user_permissions})
        colleges=College.objects.all()
        return render(request,template_name="onlineapp/colleges.html",context={'jails':colleges,'title': 'All colleges | Students App','user_permissions':user_permissions})

class AddCollegeView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        user_permissions=request.user.get_all_permissions()
        if (resolve(request.path_info).url_name == 'deletecollege_html'):
            college = College.objects.get(id=kwargs.get('collegeid')).delete()
            return redirect("colleges_html")
        obj=addcollege()
        if (kwargs):
            college=College.objects.filter(id=kwargs['collegeid']).first()
            obj=addcollege(instance=college)
        return render(request, template_name='onlineapp/register.html',context={'form':obj,'title': 'Register'})

    def post(self,request,*args,**kwargs):
        if(resolve(request.path_info).url_name=='editcollege_html'):
            college = College.objects.filter(id=kwargs['collegeid']).first()
            form=addcollege(request.POST,instance=college)
            if(form.is_valid()):
                form.save()
                return redirect("colleges_html")
        form=addcollege(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("colleges_html")

class AddStudentView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        if (resolve(request.path_info).url_name == 'deletestud_html'):
            stud = Student.objects.get(id=kwargs.get('studid')).delete()
            return redirect("students_html",kwargs.get('collegeid'))
        studs = addstudent()
        studsmarks = addmocktest()
        if (len(kwargs)>1):
            stud = Student.objects.get(id=kwargs.get('studid'))
            mock = MockTest1.objects.get(student=stud)
            studs = addstudent(instance=stud)
            studsmarks = addmocktest(instance=mock)
        return render(request, template_name='onlineapp/studentregister.html', context={'studs': studs, 'studsmarks': studsmarks, 'title': 'Studnet Register'})
    def post(self,request,*args,**kwargs):
        if (resolve(request.path_info).url_name == 'editstud_html'):
            stud = Student.objects.get(id=kwargs.get('studid'))
            mock = MockTest1.objects.get(student=stud)
            studs = addstudent(request.POST,instance=stud)
            studsmarks = addmocktest(request.POST,instance=mock)
            studs.save()
            studsmarks.save()
            return redirect("students_html",kwargs.get('collegeid'))
        col=College.objects.get(id=kwargs['collegeid'])
        stud=Student(college=col)
        form1=addstudent(request.POST,instance=stud)
        if(form1.is_valid()):
            form1.save()
            mock=MockTest1(student=stud)
            form2=addmocktest(request.POST,instance=mock)
            if form2.is_valid():
                form2.save()
            return redirect("students_html",**kwargs)


class loginuser(View):
    def get(self,request):
        if(request.user.is_authenticated):
            return redirect('colleges_html')
        login_form=loginn()
        return render(request,template_name='onlineapp/login.html',context={'form':login_form,'title':'Login User'})
    def post(self,request):
        user=request.POST['username']
        passw=request.POST['password']
        user = authenticate(username=user, password=passw)
        if user is not None:
            login(request,user)
            return redirect('colleges_html')
        else:
            messages.error(request,'Invalid-credentials')
            return redirect('login_html')
class Signupuser(View):
    def get(self,request):
        signup_form=signup()
        return  render(request,template_name='onlineapp/signup.html',context={'form':signup_form,'title':'SignUp User'})
    def post(self,request):
        form=signup(request.POST)
        if(form.is_valid()):
            user= User.objects.create_user(**form.cleaned_data)
            user.save()
            return redirect('login_html')