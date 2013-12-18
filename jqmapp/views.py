from django.views.generic import TemplateView, FormView
from django.core.cache import cache
import forms



class Demo1View(FormView):
    template_name = 'jqmapp/demo1.html'
    form_class = forms.Demo1Form
    success_url = '/demo1/'

    def form_valid(self, form):
        cache.set('servo', form.cleaned_data['servo'])
        cache.set('led1', form.cleaned_data['led1'])
        cache.set('led2', form.cleaned_data['led2'])
        return super(Demo1View, self).form_valid(form)

    def get_initial(self):
        servo = cache.get('servo', 0)
        led1 = cache.get('led1')
        led2 = cache.get('led2')
        initial = {'servo': servo, 'led1': led1, 'led2': led2}
        return initial
