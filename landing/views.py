from django.shortcuts import render
from .models import *
from .forms import LeadForm


def home(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'home.html', {'courses': courses, 'teachers': teachers})

def about(request):
    return render(request, 'about.html', {})

def course(request, pk):
    # запрос на получение определённого объекта. Обязательным аспектом является передача "условия" - pk=pk, нужно передать информацию , которая будет сравниваться с выбранным полем.
    course_data = Course.objects.get(pk=pk)
    # Первое pk= отображает значение из БД, второе pk является значением полученным с запроса
    form = LeadForm(request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False) 
        # form.save(commit=False) - приостановка автосохранения в базе данных
        is_success = True
        instance.course = course_data
        instance.save() # Сохраняем информацию в базе данных
        form = LeadForm() # Очищем форму
    return render(request, 'course.html', {'course': course_data, 'form': form, 'is_success': is_success})

def check_leads(request):
    leads = Lead.objects.all
    return render(
        request, 'leads.html',{'leads': leads}
    )

