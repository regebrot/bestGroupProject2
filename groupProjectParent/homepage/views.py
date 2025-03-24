from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from leaderboard.models import LeaderboardEntry
from django.contrib.auth.models import User

def calculate_percentile(user_score, scores):
    if not scores:
        return 0
    if user_score == max(scores):
        return 100.0
    count_lower = sum(1 for s in scores if s < user_score)
    return round((count_lower / len(scores)) * 100, 2)

def calculate_best_score_for_game(user, game):
    entry = LeaderboardEntry.objects.filter(game=game, user=user).first()
    return entry.score if entry else 0

def calculate_overall_score(user, games):
    total = 0
    for game in games:
        total += calculate_best_score_for_game(user, game)
    return total

@login_required(login_url='my-login')
def homepage(request):
    games = ["Energy Conservation", "Cycling", "Recycling", "Quiz"]
    
    game_percentiles = {}
    for game in games:
        entries = LeaderboardEntry.objects.filter(game=game)
        all_scores = [entry.score for entry in entries]
        user_score = calculate_best_score_for_game(request.user, game)
        game_percentiles[game] = calculate_percentile(user_score, all_scores)
    
    all_users = User.objects.filter(leaderboardentry__isnull=False).distinct()
    overall_scores = [calculate_overall_score(u, games) for u in all_users]
    user_overall = calculate_overall_score(request.user, games)
    overall_percentile = calculate_percentile(user_overall, overall_scores)
    
    context = {
        'energy_percentile': game_percentiles.get("Energy Conservation", 0),
        'cycling_percentile': game_percentiles.get("Cycling", 0),
        'recycling_percentile': game_percentiles.get("Recycling", 0),
        'quiz_percentile': game_percentiles.get("Quiz", 0),
        'overall_percentile': overall_percentile,
    }
    return render(request, 'home.html', context)

def about(request):
  return render(request, 'about.html')
