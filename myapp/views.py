from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponse
from .models import Student
# Create your views here.
def about(request):
    return render(request, 'about.html')

def liststudent(request):
    student = Student.objects.all()
    context = {'student' : student}
    return render(request, 'list_student.html', context)



def student(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponse("Saved...")
    context = {}
    context['form']=form
    return render(request, 'student.html', context)


def index(request):

    return render(request, 'index.html')

def second(request):
    return HttpResponse("This is second")

def pass_data(request):
    some_data = {
        "name" : "usama",
        "age" : "55"
    }

    return render(request, 'pass_data.html', context=some_data)