from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # login endpoint
    path('login', views.login_user, name='login'),
    # logout endpoint
    path('logout', views.logout_request, name='logout'),
    # register endpoint
    path('register', views.registration, name='register'),

    # Get all dealers
    path('get_dealers', views.get_dealerships, name='get_dealers'),
    # Get dealers by state
    path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),
    # Get a specific dealer
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_detail'),
    # Get reviews for a dealer
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='dealer_reviews'),
    # Add a review
    path('add_review', views.add_review, name='add_review'),
    # Get all cars
    path('get_cars', views.get_cars, name='get_cars'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
