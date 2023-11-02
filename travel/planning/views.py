from email import message
from django.shortcuts import render, redirect
from planning.models import Activities,PlaceStay,Restaurant,Location,SignUp
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RestaurantForm
from django.urls import reverse
from django.contrib.auth import login,authenticate
from .models import PlaceStay
from .forms import PlaceStayForm
from .models import Activities
from .forms import ActivitiesForm
from django.shortcuts import render, get_object_or_404
from .models import Activities, Restaurant, PlaceStay

#Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def signup(request):
    if request.method == 'POST':
        email1 = request.POST.get('email')
        password1 = request.POST.get('password')
        nickname = request.POST.get('nickname')
        phoneNo = request.POST.get('phoneNo')  # Extract the birthday from the POST request


        if SignUp.objects.filter(email=email1).exists():
            return render(request, "SignUp.html", {"message": "Email already registered."})
        else:
            user = SignUp(email=email1, password=password1, nickname=nickname, phoneNo=phoneNo)
            user.save()
            return redirect('login')

    return render(request, "SignUp.html")

def login(request):
    if request.method == 'POST':
        email2 = request.POST.get('email')
        password2 = request.POST.get('password')
        
        # Fetch the SignUp object with the provided email
        try:
            user = SignUp.objects.get(email=email2,password=password2)
            request.session['user_email'] = user.email
            return redirect('plan')
        except SignUp.DoesNotExist:
                return render(request, 'Login.html', {'error': 'Invalid Profile'})
    else:
        return render(request, 'Login.html')

def restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('restaurant')  # Redirect to the same page after adding a new restaurant
    else:
        form = RestaurantForm()

    data = Restaurant.objects.all()
    return render(request, 'restaurant.html', {'data': data, 'form': form})


def placestay(request):
    data = PlaceStay.objects.all()

    if request.method == 'POST':
        form = PlaceStayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('placestay')
    else:
        form = PlaceStayForm()

    return render(request, 'placestay.html', {'data': data, 'form': form})

def activities(request):
    data = Activities.objects.all()

    if request.method == 'POST':
        form = ActivitiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activities')
    else:
        form = ActivitiesForm()

    return render(request, 'activities.html', {'data': data, 'form': form})

def plan(request):
    activities = Activities.objects.all()
    restaurants = Restaurant.objects.all()
    placestays = PlaceStay.objects.all()
    return render(request, 'plan.html', {'activities': activities, 'restaurants': restaurants, 'placestays': placestays})

def selected_results(request):
    if request.method == 'POST':
        activities_id = request.POST['activities']
        restaurant_id = request.POST['restaurant']
        placestay_id = request.POST['placestay']

        activity = Activities.objects.get(activities_id=activities_id)
        restaurant = Restaurant.objects.get(restaurant_id=restaurant_id)
        placestay = PlaceStay.objects.get(place_id=placestay_id)

        return render(request, 'selected_results.html', {'activity': activity, 'restaurant': restaurant, 'placestay': placestay})
    else:
        return render(request, 'plan.html')
    
def user_detail(request):
    # Check if user is logged in
    if 'user_email' in request.session:
        user_email = request.session['user_email']
        try:
            # Get user details based on the logged in user's email
            user = SignUp.objects.get(email=user_email)
            return render(request, 'user_detail.html', {'user': user})
        except SignUp.DoesNotExist:
            return render(request, 'user_detail.html', {'error': 'User not found'})
    else:
        # Redirect to login page if user is not logged in
        return redirect('login')

def delete_activity(request,activities_id):
    data = Activities.objects.get(activities_id=activities_id)
    data.delete()
    return HttpResponseRedirect(reverse('activity'))

def delete_restaurant(request,restaurant_id):
    data = Restaurant.objects.get(restaurant_id=restaurant_id)
    data.delete()
    return HttpResponseRedirect(reverse('restaurant'))

def delete_plastay(request,place_id):
    data = PlaceStay.objects.get(place_id=place_id)
    data.delete()
    return HttpResponseRedirect(reverse('placestay'))

