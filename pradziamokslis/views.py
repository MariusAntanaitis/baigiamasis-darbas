from django.shortcuts import render
from django.views import View
from datetime import datetime
from pradziamokslis.models import Mokinys
from pradziamokslis.forms import MokinysForm
from pradziamokslis.utils.utils import calculate
from django.views.generic.edit import UpdateView, DeleteView, FormView
# Create your views here.

class HomepageView(View):
    template_name = "home.html"

    def get(self, request):
        now = datetime.now()
        date_time = now.strftime("%Y/%m/%d, %H:%M:%S")
        pamoku_listas = ["Kintamieji", "Masyvai, ciklai", "Funkcijos", "Objektinis programavimas", "class metodas", 
        "GUI", "Loginimas", "Duomenu bazes", "Info traukimas is interneto(Web scraping)", "Flask"]

        return render(request, self.template_name, {'date_time': date_time, 'pamoku_listas': pamoku_listas})


class StudentsListView(View):
    template_name = "students-list.html"

    def get(self, request):
        mokiniu_sarasas = Mokinys.objects.all()

        return render(request, self.template_name, {'mokiniu_sarasas': mokiniu_sarasas})


class MokinysCreateView(FormView):
    template_name = 'mokinys_form.html'
    form_class = MokinysForm
    success_url = '/mokiniai'

    def form_valid(self, form):

        form.save()
        return super().form_valid(form)

class MokinysUpdateView(UpdateView):
    model = Mokinys
    template_name = 'mokinys_form.html'
    success_url = '/mokiniai'
    fields = '__all__'

class MokinysDeleteView(DeleteView):
    model = Mokinys
    template_name = 'mokinys_delete.html'
    success_url = '/mokiniai'

class MathView(View):
    template_name = "math.html"

    def get(self, request):
        
        return render(request, self.template_name)

    def post(self, request):
        number1 = int(request.POST['number1'])
        number2 = int(request.POST['number2'])
        action = request.POST["action"]
        result = calculate(number1, number2, action)
        return render(request, self.template_name, {"result": result})

