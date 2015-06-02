from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=30)
    rating = models.FloatField()
    length = models.SmallIntegerField()
    def __str__(self):
       	 return self.name
    def __hash_(self):
        return hash(self.__str__())



class Projection(models.Model):
    movie_id = models.ForeignKey(Movie)
    type = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return "{} {} {} {}".format(self.movie_id.name, self.type, self.date, self.time)

    def __hash_(self):
        return hash(self.__str__())

class Reservation(models.Model):
    username = models.CharField(max_length=30)
    projection_id = models.ForeignKey(Projection)
    row = models.SmallIntegerField()
    col = models.SmallIntegerField()
    def __str__(self):
        return "{} {} {}".format(str(self.projection_id),self.row, self.col)


class User(models.Model):
    username = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

    def __str__(self):
        return '{} {}'.format(self.username, self.email)
