from django.contrib import admin
from .models import Movie, Reservation, Projection, User

admin.site.register(Movie)
admin.site.register(Reservation)
admin.site.register(Projection)
admin.site.register(User)
