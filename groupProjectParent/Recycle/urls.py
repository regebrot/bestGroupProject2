from django.urls import path

from .views import add5, pictures1, wrong, next_image, pictures3, pictures4, pictures5, pictures6, pictures7, pictures8, pictures9, pictures10, leaderboards

urlpatterns = [
 path("pictures/", pictures1, name="pictures"),
 path("pictures/add5", add5, name="add5"),
 path("pictures/wrong", wrong, name="wrong"),
 path("pictures/next_image", next_image, name="pictures2"),
 path("pictures/leaderboards/", leaderboards, name="leaderboards"),
 path("pictures/pictures3", pictures3, name="pictures3"),
 path("pictures/pictures4", pictures4, name="pictures4"),
 path("pictures/pictures5", pictures5, name="pictures5"),
 path("pictures/pictures6", pictures6, name="pictures6"),
 path("pictures/pictures7", pictures7, name="pictures7"),
 path("pictures/pictures8", pictures8, name="pictures8"),
 path("pictures/pictures9", pictures9, name="pictures9"),
 path("pictures/pictures10", pictures10, name="pictures10"),
 path("pictures2/add5", add5, name="add5"),
 path("pictures2/wrong", wrong, name="wrong"),
 path("correct", add5),
]