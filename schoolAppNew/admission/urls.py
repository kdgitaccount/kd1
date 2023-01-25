from django.urls import path
from admission.views import addAdmissions
from admission.views import admissionReport
from admission.views import addVendor
from admission.views import deleteStudent
from admission.views import updateStudent
from admission.views import FirstClassBasedView
from admission.views import TeacherRead
from admission.views import getTeacherRead
from admission.views import AddTeacher
from admission.views import UpdateTeacher
from admission.views import RemoveTeacher
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('newadm/', addAdmissions),
    path('admreport/', admissionReport),
    path('addven/',addVendor),
    path('delete/<int:id>', deleteStudent),
    path('update/<int:id>', updateStudent),
    path('firstcbv/',FirstClassBasedView.as_view()),
    path('teacherslist/',login_required(TeacherRead.as_view()),name='listteachers'),
    path('getteacherdetails/<int:pk>/',login_required(getTeacherRead.as_view()), name='getteacherinfo'),
    path('insertteacher/',login_required(AddTeacher.as_view())),
    path('updateteacher/<int:pk>/',login_required(UpdateTeacher.as_view())),
    path('deleteteacher/<int:pk>/',login_required(RemoveTeacher.as_view())),


]
