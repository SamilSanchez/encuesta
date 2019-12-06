# Django
from django.urls import path

# Views
from . import views

def my_custom_page_not_found_view(request, exception=None):
    import pudb; pudb.set_trace()
    return HttpResponse('Error handler 404', status=404)


urlpatterns = [
    # ex: /polls/
    path('', views.index, name= 'index'),
    # ex: /polls/5
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:quesion_id>/results', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]

# handler404 = 'mysite.views.my_custom_page_not_found_view'
handler404 = my_custom_page_not_found_view


