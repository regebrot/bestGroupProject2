from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Max
from .models import LeaderboardEntry
from .utils import update_badges
from django.contrib.auth.decorators import login_required

@login_required(login_url='my-login')
def leaderboard_view(request):
    update_badges()
    games = ["Energy Conservation", "Recycling", "Cycling", "Quiz"]
    
    leaderboard_data = []
    
    users = User.objects.filter(leaderboardentry__isnull=False).distinct()
    for user in users:
        display_name = user.profile.display_name if user.profile.display_name else user.username
        user_row = {"display_name": display_name}
        overall = 0
        for game in games:
            best_score = LeaderboardEntry.objects.filter(user=user, game=game).aggregate(Max('score'))['score__max'] or 0
            user_row[game] = best_score
            overall += best_score
        user_row["overall"] = overall
        leaderboard_data.append(user_row)

    leaderboard_data.sort(key=lambda x: x["overall"], reverse=True)
    
    context = {
        "leaderboard_data": leaderboard_data,
        "games": games
    }
    return render(request, "leaderboards.html", context)
