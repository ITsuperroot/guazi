
from django.template import Template
# Create your views here.
from django.shortcuts import reverse
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.views import View
from django.template.loader import get_template
import datetime , time
from django.db.models import F
from .models import Car , Owner, Basic_parameter, Engine_parameter,Chassis_braking
from django.views import generic
# class Detail(View):
#     def get(self , request ):
#         todos = Car.objects.all()
#         return render(request, 'details/chassis_braking.html', {'todos':todos})
class CarView(View):
    def get(self , request , pk):
        car = Car.objects.get(id = pk)
        context_object_name = car
        car1 = car.price * 40
        if car1 <=3500:
            car1=3500

        return render(request, 'details/_car.html',{'car':car, 'car1':car1})

# def car(request, car_id):
#     car = get_object_or_404(Car, pk=car_id)





# class CarView(generic.DetailView):
#     context_object_name = 'car'
#     template_name = 'details/_car.html'
#     def get_queryset(self , car_id):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return Car.objects.filter(id = car_id)

# class CarView(generic.DetailView):
#     template_name = 'details/_car.html'
#     def get_queryset(self):
#         return Car.objects.filter(id=car_id)
# def car(request, car_id):
     # car1 = F('price')*0.04

        # if car1 <= 3500:
        #     return render(request, 'details/_car.html', {'car': car}, {'car1': 3500})
        #
        # else :
        #     pass