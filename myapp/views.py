from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import FoodEntry

# Create your views here.
def index(request):
    context = {"message" : "Welcome to Django!"}
    return render(request, 'index.html')


def dashboard(request):
    return render(request, "dashboard.html")

@csrf_exempt  
@require_POST
def add_food(request):
    name = request.POST.get("newFood")
    calories = request.POST.get("newFoodCals")

    if not name or not calories:
        return JsonResponse({"error": "Invalid data"}, status=400)

    entry = FoodEntry.objects.create(
        name=name,
        calories=int(calories)
    )

    return JsonResponse({
        "id": entry.id,
        "name": entry.name,
        "calories": entry.calories,
        "date": entry.date,
        "time": entry.time
    })
