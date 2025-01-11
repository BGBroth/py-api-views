from django.urls import path
from rest_framework.routers import DefaultRouter
from cinema.views import (
    MovieViewSet,
    GenreList,
    GenreDetail,
    CinemaHallList,
    CinemaHallDetail,
    ActorList,
    ActorDetail
)

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

app_name = "cinema"

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallList.as_view(), name="actor-list"),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallDetail.as_view(),
        name="actor-detail"
    ),
] + router.urls
