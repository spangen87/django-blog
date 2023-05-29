from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import Leaderboard


def memory(request):
    """
    Render the game
    """
    template = 'memory.html'

    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }

    return render(request, template, context)


@csrf_exempt
def save_leaderboard(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        score = int(request.POST.get('score'))
        
        time = request.POST.get('time')
        try:
            time = int(time)
        except (ValueError, TypeError):
            time = 0  # Set a default value or handle the error accordingly
        
        leaderboard = Leaderboard(name=name, email=email, score=score, time=time)
        leaderboard.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})
