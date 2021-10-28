from django.shortcuts import render
from django.http import JsonResponse

from .models import Students

# Create your views here.

def index(request):
    students = Students.objects.all()
    students = {'students': students}

    return render(request, 'index.html', students)


def api(request):
    students = Students.objects.all().values()

    return JsonResponse(list(students), safe=False)
