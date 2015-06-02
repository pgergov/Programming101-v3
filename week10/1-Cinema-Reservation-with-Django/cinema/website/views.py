from django.shortcuts import render, redirect
from .forms import UserPassForm
from django.http import HttpResponse
from .models import Movie, Projection, Reservation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .create_room import creator

def index(request):
    return render(request, 'index.html', {'username':'Account','complete':'ind.html',
                                          'class1': 'active', 'class2': '',
                                          'log':'/login', 'log_name': 'Sign in'})

def reservation(request):
    if not request.user.is_authenticated():
        return redirect('login')
    class1=""
    class2=""
    class3="active"
    make_reg = "Make Reservation"
    username = request.user
    log_name = 'Sign out'
    complete = 'reservation.html'
    movies = Movie.objects.all()
    log = '/logout'
    lst =dict()
    for movie in movies:
        lst[movie]=movie.projection_set.all()
    movies = lst
    for ky in lst.keys():
        print("{} {}".format(ky, lst[ky]))
    return render(request, 'index.html', locals())

def login_tmp(request):
    alert = 'empty.html'
    return render(request, 'login.html', locals())

def completed(request):
    if request.method == 'POST':
        req = request.POST.keys()
        usrname = request.user
        proj_id = request.POST.get('proj_id')
        projection = Projection.objects.get(id=proj_id)
        print(projection)
        seats = []
        for reqst in req:
            try:
                seats.append(int(reqst))
            except:
                pass
        for seat in seats:
            row = seat // 10
            col = seat % 10
            res = Reservation(username=usrname, 
                              projection_id=projection,
                              row=row,
                              col=col
                              )
            res.save()
        return account(request)

def account(request):
   complete='user_profile.html'
   username = request.user
   make_reg = 'Make Reservation'
   log = '/logout'
   complete = 'user_profile.html'
   log_name = 'Sign out'
   reservs = Reservation.objects.filter(username=username).all()
   return render(request, 'index.html', locals())


def submit(request):
    if request.method == 'POST':
        req = request.POST
        user = req['user']
        password = req['pass'] 
        usr = authenticate(username=user, password=password)
        if usr is not None:
            login(request, usr)
            complete='user_profile.html'
            username = user
            make_reg = 'Make Reservation'
            log = '/logout'
            complete = 'user_profile.html'
            log_name = 'Sign out'
            return account(request)
        else:
            alert = 'alert.html'
            return render(request, 'login.html', locals())
    else:
        return HttpResponse("Nice Try!")


def logout_tmp(request):
    logout(request)
    return index(request)

def get_reserv(request):
    projection = Projection.objects.filter(pk=request.GET['proj_id']).first()
    reservs = projection.reservation_set.all()
    class1=""
    class2=""
    class3="active"
    make_reg = "Make Reservation"
    username = request.user
    log_name = 'Sign out'
    complete = 'room.html'
    log = '/logout'
    p=-1
    taken = []
    reservs = Reservation.objects.filter(projection_id=projection)
    for reserv in reservs:
        taken.append((reserv.row, reserv.col))
    creator(taken, request.GET['proj_id'])
    return render(request, 'index.html', locals())



def register(request):
    if request.method == 'POST':
        req = request.POST
        user = req['user']
        passw = req['pass']
        email = req['email']
        try:
            usr = User.objects.create_user(username=user, password=passw, email=email)
        except Exception:
            alert = 'reg_alert.html'
            return render(request, 'register.html', locals())
        return index(request)
    alert = 'empty.html'
    return render(request, 'register.html', locals())

def movies(request):
    movies = list(Movie.objects.all())
    return render(request, 'index.html', {'complete': 'movies.html','movies_list': movies,
                                         'class1': '', 'class2': 'active',
                                          'log': '/login', 'log_name': 'Sign in', 'username':'Account'})

