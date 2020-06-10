from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Plant, Demand, Function
from django.template import loader
# Create your views here.


def optimize(request):
    plant = get_object_or_404(Plant, plant_name='Plant 2')
    all_plants_list = Plant.objects.all()
    context = {
            'all_plants_list': all_plants_list,
    }
    return render(request, 'calculator/main.html', context)

def choosePlants(request):
    all_plants_list = Plant.objects.all()
    all_demands_list = Demand.objects.all()
    all_functions_list = Function.objects.all()
    context = {
        'all_plants_list': all_plants_list,
        'all_demands_list': all_demands_list,
        'all_functions_list': all_functions_list,

    }
    return render(request, 'calculator/choices.html', context )

    #
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

def chooseDemands(request):
    return HttpResponse("Choosing Demands")

def chooseModel(request):
    return HttpResponse("Choosing Model")


from .optimizer import optimizeFunction

def updateChoices(request):
    plant_variable = request.POST.getlist('plants')
    # print(plant_variable)
    demand_variable = request.POST.getlist('demands')
    # print(demand_variable)
    function_variable = request.POST.getlist('functions')
    # print(function_variable)
    input_name = request.POST.get('Layout_Name')
    
    optimizeFunction(plant_variable, demand_variable, function_variable, input_name)

    return HttpResponse("It Worked!")
