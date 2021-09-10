from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('lead/',views.LeadListView.as_view(),name='leadlist')

]
