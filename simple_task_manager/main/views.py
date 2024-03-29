from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from datetime import date, timedelta
from simple_task_manager.main.models import ArchiveReport, Category, Event
from simple_task_manager.main.forms import EventForm, ReportForm


@login_required
def home(request):
    incedents = Event.objects.filter(category__name='Инцидент').filter(archive_report=None)
    currents_activity = Event.objects.filter(category__name='Текущая').filter(archive_report=None)
    completed_activity = Event.objects.filter(category__name='Выполненная').filter(archive_report=None)
    hr_events = Event.objects.filter(category__name='По персоналу').filter(archive_report=None)
    last_monday = date.today() - timedelta(days=date.today().weekday(), weeks=1)
    last_friday = last_monday + timedelta(days=4)
    return render(request, 'home.html', context={
        'incedents': incedents,
        'currents_activity': currents_activity,
        'completed_activity': completed_activity,
        'hr_events': hr_events,
        'event_form': EventForm(),
        'report_form': ReportForm(
            initial={
                'start_date': '{:%Y-%m-%d}'.format(last_monday),
                'end_date': '{:%Y-%m-%d}'.format(last_friday),
            }),
    })


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, message='Ошибка заполнения формы!')
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


@transaction.atomic
def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            archive_events = Event.objects.filter(archive_report=None).filter(
                created_at__gte=start_date).filter(created_at__lte=end_date)
            try:
                archive_report = ArchiveReport.objects.get(
                    start_date=start_date, end_date=end_date)
            except ArchiveReport.DoesNotExist:
                archive_report = form.save()
            archive_events.update(archive_report=archive_report)
    return redirect('home')
