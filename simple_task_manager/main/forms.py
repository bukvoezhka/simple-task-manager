from django.forms import ModelForm, Select, Textarea
from simple_task_manager.main.models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['category', 'description']
        widgets = {
            'category': Select(attrs={
                'class': 'form-select',
                'size': '5',
                'aria-label': 'category selection',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'rows': '8',
                'aria-label': 'category description',
            })}

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['category'].initial = 0
