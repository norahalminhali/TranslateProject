from django.db import models

# Create your models here.


#Translator location model
class Country(models.Model):
    name = models.CharField(max_length=200, unique= True)
    flag = models.ImageField(upload_to="images/")

class City(models.Model):
    name = models.CharField(max_length=200, unique= True)
    #one to many relationship
    country = models.ForeignKey( Country, on_delete= models.CASCADE)


class Translator(models.Model):
    
    class LanguageChoices(models.TextChoices):
        ARABIC = "arabic", "Arabic"
        ENGLISH = "english", "English"
        KOREAN = "korean", "Korean"
        CHINESE = "chinese", "Chinese"
        JAPANESE = "japanese", "Japanese"
        OTHER = "other", "Other"

    class RatingChoices(models.IntegerChoices):
        STAR1 = 1, "One Star"
        STAR2 = 2, "Two Stars"
        STAR3 = 3, "Three Stars"
        STAR4 = 4, "Four Stars"
        STAR5 = 5, "Five Stars"

    name = models.CharField(max_length=200, unique= True)
    language = models.CharField(max_length=50, choices= LanguageChoices.choices)
    specialty = models.CharField(max_length=200)
    experience = models.TextField()
    rating = models.SmallIntegerField(choices=RatingChoices.choices)
    created_at = models.DateTimeField(auto_now=True)
    #location - one to many relationship
    country = models.ForeignKey( Country, on_delete=models.CASCADE )

class Review(models.Model):

    name = models.CharField(max_length=1024)
    rating = models.SmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField( auto_now_add= True )

    #one to many relationship
    translator = models.ForeignKey( Translator, on_delete=models.CASCADE )