from django.shortcuts import redirect, render
from simple_task_manager.main.models import ArchiveReport, Category, Event
from simple_task_manager.main.forms import EventForm


def home(request):
    incedents = Event.objects.filter(category__name='Инцидент').filter(archive_report=None)
    currents_activity = Event.objects.filter(category__name='Текущая').filter(archive_report=None)
    completed_activity = Event.objects.filter(category__name='Выполненная').filter(archive_report=None)
    hr_events = Event.objects.filter(category__name='По персоналу').filter(archive_report=None)
    return render(request, 'home.html', context={
        'incedents': incedents,
        'currents_activity': currents_activity,
        'completed_activity': completed_activity,
        'hr_events': hr_events,
        'form': EventForm()
    })


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home')


def delete_event(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect('home')


def archive(request):
    archive_reports = ArchiveReport.objects.all()
    categories = Category.objects.all()
    return render(request, 'archive.html', context={
        'archive_reports': archive_reports,
        'categories': categories,
    })
