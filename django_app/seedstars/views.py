from django.shortcuts import render
from django.views import generic

from .models import Person
from .forms import PersonForm


class IndexView(generic.TemplateView):
    template_name = "seedstars/index.html"


class ListView(generic.View):
    model = Person
    template_name = 'seedstars/list.html'

    def get(self, request):
        person_list = Person.objects.all()
        context = {'persons' : person_list}
        return render(request, self.template_name, context)


class AddView(generic.View):

    form_class = PersonForm
    template_name = 'seedstars/add.html'

    context = {}
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context = {'form' : form}
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = self.form_class(request.POST)
        self.context = {'form' : form}
        if form.is_valid():
            form.save(commit=True)
            self.context['success_message'] = "Record Successfully Added!"
            return render(request, self.template_name, self.context)

        return render(request, self.template_name, self.context)

