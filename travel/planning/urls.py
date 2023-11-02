from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('placestay/', views.placestay, name='placestay'),
    path('activities/', views.activities, name='activities'),
    path('plan/', views.plan, name='plan'),
    path('selected_results/', views.selected_results, name='selected_results'),
    path('user_detail/', views.user_detail, name='user_details'),
    path('restaurant/delete_restaurant/<str:restaurant_id>',views.delete_restaurant,name='delete_restaurant'),
    path('activities/delete_activity/<str:activities_id>',views.delete_activity,name='delete_activities'),
    path('placestay/delete_placestay/<str:place_id>',views.delete_plastay,name='delete_placestay'),
]