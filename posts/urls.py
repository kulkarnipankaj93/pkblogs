from django.urls import path
from .views import index, post_details

app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:post_slug>', post_details, name='details')
    # path('post/<int:post_id>', post_details, name='details')
]