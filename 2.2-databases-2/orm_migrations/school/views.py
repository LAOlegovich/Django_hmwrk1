from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    data = Student.objects.prefetch_related('teachers').all()
    context = {'object_list':data}

    return render(request, template, context)
