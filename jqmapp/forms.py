from django import forms

SWITCH_CHOICES = (
    (False, 'Off'),
    (True, 'On'),
)

class Demo1Form(forms.Form):
    led1 = forms.TypedChoiceField(label=u'Led 1', coerce=lambda x: x == 'True',
                                choices=SWITCH_CHOICES, widget=forms.Select(attrs={'data-role': 'slider', }))
    led2 = forms.TypedChoiceField(label=u'Led 2', coerce=lambda x: x == 'True',
                                choices=SWITCH_CHOICES, widget=forms.Select(attrs={'data-role': 'slider', }))
    servo = forms.IntegerField(min_value=0, max_value=60, label="Servo rotation",
                               widget=forms.widgets.NumberInput(attrs={'type': 'range', 'data-highlight': 'true'}))
