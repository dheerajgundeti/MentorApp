from django.urls import path, include
from onlineapp.views import *
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    #path('get_all_colleges/',get_all_colleges),
    #path('college_students_info/<int:collegeid>/',college_students_info),
    path('test_view/',my_first_view),

    path('api/v1/token',obtain_auth_token,name="gettoken"),

    path("api/v1/college/",rest_college),
    path("api/v1/college/<int:clgid>/",rest_college_i),


    path("", lambda req : redirect('login_html')),

    path('colleges/',CollegeView.as_view(),name='colleges_html'),
    path('colleges/<int:collegeid>',CollegeView.as_view(),name='students_html'),


    path('colleges/add',AddCollegeView.as_view(),name='addcollege_html'),
    path('colleges/<int:collegeid>/edit',AddCollegeView.as_view(),name='editcollege_html'),
    path('colleges/<int:collegeid>/delete',AddCollegeView.as_view(),name='deletecollege_html'),

    path('colleges/<int:collegeid>/add',AddStudentView.as_view(),name='addstud_html'),
    path('colleges/<int:collegeid>/<int:studid>/edit/',AddStudentView.as_view(),name='editstud_html'),
    path('colleges/<int:collegeid>/<int:studid>/delete/', AddStudentView.as_view(), name='deletestud_html'),


    path('login/',loginuser.as_view(),name='login_html'),
    path('signup/',Signupuser.as_view(),name='signup_html'),
    path('error_login/',loginuser.as_view(),name='error_login_html'),
    path('logout/',logout_user,name='logout_html')
]
