import logging
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from .models import CarModel
from .restapis import get_request, analyze_review_sentiments, post_review

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create an `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return HttpResponse(json.dumps(data), content_type='application/json')


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    username = request.user.username
    logout(request)
    data = {"userName": username}
    return HttpResponse(json.dumps(data), content_type='application/json')


# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False
    email_exist = False
    try:
        User.objects.get(username=username)
        username_exist = True
    except Exception:
        logger.debug("{} is new user".format(username))

    if not username_exist:
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email
        )
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        data = {"userName": username, "error": "Already Registered"}
        return HttpResponse(json.dumps(data), content_type='application/json')


def get_dealerships(request, state="All"):
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = "/fetchDealers/" + state
    dealerships = get_request(endpoint)
    return HttpResponse(json.dumps(dealerships), content_type='application/json')


def get_dealer_details(request, dealer_id):
    if dealer_id:
        endpoint = "/fetchDealer/" + str(dealer_id)
        dealership = get_request(endpoint)
        return HttpResponse(json.dumps(dealership), content_type='application/json')
    else:
        return HttpResponse(json.dumps({"status": 400, "message": "Bad Request"}), content_type='application/json')


def get_dealer_reviews(request, dealer_id):
    if dealer_id:
        endpoint = "/fetchReviews/dealer/" + str(dealer_id)
        reviews = get_request(endpoint)
        for review_detail in reviews:
            response = analyze_review_sentiments(review_detail['review'])
            print(response)
            review_detail['sentiment'] = response.get('sentiment', 'neutral') if response else 'neutral'
        return HttpResponse(json.dumps(reviews), content_type='application/json')
    else:
        return HttpResponse(json.dumps({"status": 400, "message": "Bad Request"}), content_type='application/json')


def get_cars(request):
    count = CarModel.objects.filter().count()
    print(count)
    if count == 0:
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.car_make.name,
            "CarYear": car_model.year.strftime('%Y') if car_model.year else "N/A"
        })
    return HttpResponse(json.dumps({"CarModels": cars}), content_type='application/json')


@csrf_exempt
def add_review(request):
    if request.user.is_anonymous:
        return HttpResponse(json.dumps({"status": 403, "message": "Unauthorized"}), content_type='application/json')
    data = json.loads(request.body)
    try:
        response = post_review(data)
        return HttpResponse(json.dumps({"status": 200}), content_type='application/json')
    except Exception as e:
        return HttpResponse(json.dumps({"status": 401, "message": "Error in posting review"}), content_type='application/json')


def initiate(request=None):
    from .models import CarMake, CarModel
    from datetime import date

    makes = [
        CarMake(name="Toyota", description="Japanese automaker", country_of_origin="Japan", founded_year=1937),
        CarMake(name="Ford", description="American automaker", country_of_origin="USA", founded_year=1903),
        CarMake(name="Chevrolet", description="American automaker", country_of_origin="USA", founded_year=1911),
        CarMake(name="BMW", description="German automaker", country_of_origin="Germany", founded_year=1916),
        CarMake(name="Honda", description="Japanese automaker", country_of_origin="Japan", founded_year=1946),
    ]
    for make in makes:
        make.save()

    toyota = CarMake.objects.get(name="Toyota")
    ford = CarMake.objects.get(name="Ford")
    chevrolet = CarMake.objects.get(name="Chevrolet")
    bmw = CarMake.objects.get(name="BMW")
    honda = CarMake.objects.get(name="Honda")

    models = [
        CarModel(car_make=toyota, name="Camry", car_type="SEDAN", year=date(2022, 1, 1), dealer_id=1, seats=5),
        CarModel(car_make=toyota, name="RAV4", car_type="SUV", year=date(2023, 1, 1), dealer_id=1, seats=5),
        CarModel(car_make=ford, name="Mustang", car_type="COUPE", year=date(2022, 1, 1), dealer_id=2, seats=4),
        CarModel(car_make=ford, name="F-150", car_type="TRUCK", year=date(2023, 1, 1), dealer_id=2, seats=6),
        CarModel(car_make=chevrolet, name="Malibu", car_type="SEDAN", year=date(2022, 1, 1), dealer_id=3, seats=5),
        CarModel(car_make=chevrolet, name="Equinox", car_type="SUV", year=date(2023, 1, 1), dealer_id=3, seats=5),
        CarModel(car_make=bmw, name="3 Series", car_type="SEDAN", year=date(2022, 1, 1), dealer_id=4, seats=5),
        CarModel(car_make=bmw, name="X5", car_type="SUV", year=date(2023, 1, 1), dealer_id=4, seats=7),
        CarModel(car_make=honda, name="Accord", car_type="SEDAN", year=date(2022, 1, 1), dealer_id=5, seats=5),
        CarModel(car_make=honda, name="CR-V", car_type="SUV", year=date(2023, 1, 1), dealer_id=5, seats=5),
    ]
    for model in models:
        model.save()
