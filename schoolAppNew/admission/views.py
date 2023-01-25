from django.shortcuts import render
from admission.models import student
from admission.forms import studentModelForm
from admission.forms import vendorForm
from django.views.generic import View, ListView, DetailView, CreateView,UpdateView, DeleteView
from django.http import HttpResponse
from admission.models import Teacher
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
class FirstClassBasedView(View):
    def get(self,request):
        return HttpResponse("<h1>Hello...This is first class based view</h1>")


class TeacherRead(ListView):
    model = Teacher

def logoutuser(request):
    return render(request, 'logout.html')

class getTeacherRead(DetailView):
    model = Teacher


class AddTeacher(CreateView):
    model = Teacher
    fields = ('name', 'experience', 'subject', 'contact')


class UpdateTeacher(CreateView):
    model = Teacher
    fields = ('name', 'subject', 'contact')


class RemoveTeacher(DeleteView):
    model = Teacher
    success_url = reverse_lazy('listteachers')

@login_required
def homepage(request):
    return render(request, 'index.html')

@login_required
def addAdmissions(request):
    form = studentModelForm
    studentform = {'form':form}
    if request.method =="POST":
        form = studentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)

    return render(request, 'admission/addAdmission.html', studentform);

@login_required
def admissionReport(request):
    result = student.objects.all()
    Student = {"allstudents": result}

    return render(request, 'admission/admissionsreport.html', Student);

@login_required
def deleteStudent(request,id):
    s = student.objects.get(id = id)
    s.delete()
    return admissionReport(request)

@login_required
def updateStudent(request,id):
    s = student.objects.get(id = id)
    form = studentModelForm(instance = s)
    dict = {'form':form}

    if request.method =="POST":
        form = studentModelForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
        return admissionReport(request)
    return render(request, 'admission/update-admission.html', dict)

@login_required
def addVendor(request):
    form = vendorForm
    vform = {'form':form}
    if request.method =="POST":
        form = studentModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['address'])
            print(form.cleaned_data['contact'])
            print(form.cleaned_data['item'])
            print(form.cleaned_data['numberOfItems'])
            print(form.cleaned_data['MRP_Rate'])

        return homepage(request)

    return render(request, 'admission/addVendor.html', vform );
