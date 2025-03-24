from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import leaderboard
from django.db.models import F

# Create your views here.
def pictures1(request):
  return render(request, "pictures.html", {})

@login_required
def add5(request):
  leaderboard.objects.filter(username=request.user).update(points=F('points') + 5)
  return render(request, "correct.html", {})


def leaderboards(request):
  all_members = leaderboard.objects.all().order_by('-points')
  return render(request, "leaderboards.html", {'all': all_members})


@login_required
def wrong(request):
  return render(request, "incorrect.html", {})

def next_image(request):
  return render(request, "pictures2.html", {})

def pictures3(request):
  return render(request, "pictures3.html", {})

def pictures4(request):
  return render(request, "pictures4.html", {})


def pictures5(request):
  return render(request, "pictures5.html", {})

def pictures6(request):
  return render(request, "pictures6.html", {})

def pictures7(request):
  return render(request, "pictures7.html", {})

def pictures8(request):
  return render(request, "pictures8.html", {})

def pictures9(request):
  return render(request, "pictures9.html", {})

def pictures10(request):
  return render(request, "pictures10.html", {})
