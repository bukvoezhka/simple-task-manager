from django.shortcuts import redirect, render
from simple_task_manager.main.models import ArchiveReport, Event
from simple_task_manager.main.forms import EventForm


def home(request):
    incedents = Event.objects.filter(category__name='Инцидент', archive_report=True)
    currents_task = Event.objects.filter(category__name='Текущая', archive_report=True)
    completed_task = Event.objects.filter(category__name='Выполненная', archive_report=True)
    hr_events = Event.objects.filter(category__name='По персоналу', archive_report=True)
    return render(request, 'base.html', context={
        'incedents': incedents,
        'currents_activity': currents_task,
        'completed_activity': completed_task,
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
    try:
        event.delete()
    except:
        pass
    return redirect('home')


def archive(request):
    archive_reports = ArchiveReport.objects.all()
    return render(request, 'archive.html', context={
        'archive_reports': archive_reports,
    })
