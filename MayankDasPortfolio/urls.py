from django.contrib import admin
from django.urls import path
from MayankDasPortfolio import views

urlpatterns = [
    path("", views.index, name="index"),
    path("portfolio-details-gui", views.gui, name="portfolio-details-gui"),
    path("portfolio-details-web", views.web, name="portfolio-details-web"),
    path("portfolio-details-card", views.card, name="portfolio-details-card"),
]