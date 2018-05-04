from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/spec/5/
    path('spec/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/spec/5/results/
    path('spec/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/spec/5/vote/
    path('spec/<int:question_id>/vote/', views.vote, name='vote'),
]
