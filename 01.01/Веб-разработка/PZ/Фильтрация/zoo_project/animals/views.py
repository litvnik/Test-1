from django.shortcuts import render
from .models import Mammal, Bird

# Create your views here.
def animal_list(request):
    # Получаем параметры из GET-запроса
    habitat = request.GET.get('habitat')
    bird_name = request.GET.get('bird_name')

    mammals = Mammal.objects.all()
    birds = Bird.objects.all()

    # Фильтрация по месту обитания (для всех)
    if habitat:
        mammals = mammals.filter(habitat=habitat)
        birds = birds.filter(habitat=habitat)

    # Фильтрация птиц по названию
    if bird_name:
        birds = birds.filter(name__icontains=bird_name)

    # Собираем уникальные места обитания для выпадающего списка
    all_habitats = set(
        list(Mammal.objects.values_list('habitat', flat=True)) +
        list(Bird.objects.values_list('habitat', flat=True))
    )

    context = {
        'mammals': mammals,
        'birds': birds,
        'habitats': sorted(all_habitats),
        'selected_habitat': habitat,
        'bird_name_query': bird_name or '',
    }
    return render(request, 'animals/index.html', context)