from django.urls import path
from . import views
from .views import unique_employee_ids


urlpatterns = [

    path(
        'Firstapp/',
        views.employee_list
    ),
   path('unique-ids/', unique_employee_ids),


    path(
        'Firstapp/<int:id>/',
        views.employee_detail
    ),

    
    path('deleted/', 
        views.deleted_employee_list
    ),

]