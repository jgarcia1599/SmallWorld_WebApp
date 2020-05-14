

from django.conf.urls import url
from . import views

from django.views.generic import TemplateView

#dot means same directory
#
urlpatterns = [




    url(r'^role/$', views.ChooseRoleView.as_view(), name='role'),

    url(r'^role/student/$', views.StudentSignUpView.as_view(), name='signup-student'),

    url(r'^role/mentor/$', views.MentorSignUpView.as_view(), name='signup-mentor'),

    url(r'^login/$', views.LoginView.as_view(), name='login'),

    url(r'^user_profile/$', views.UserProfileView.as_view(), name='user_profile'),
    url(r'^user_profile/$', views.UserProfileView.as_view(), name='user_profile'),

]





#
# from django.urls import include, path
#
# from classroom.views import classroom, students, teachers
#
# urlpatterns = [
#     path('', include('classroom.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
#     path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
#     path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
# ]