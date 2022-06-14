from django.forms import DateInput, ModelForm, Select, Textarea
from simple_task_manager.main.models import Event, ArchiveReport


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['category', 'description']
        widgets = {
            'category': Select(attrs={
                'class': 'form-select',
                'size': '4',
                'aria-label': 'category selection',
                'required': 'True'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'rows': '8',
                'aria-label': 'category description',
            })}

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = None


class DateInput(DateInput):
    input_type = 'date'


class ReportForm(ModelForm):
    class Meta:
        model = ArchiveReport
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'end_date': DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }
