from django.contrib import admin
from .models import Language, Country, City, Translator, Review, specialty

# Register your models here.
class TranslatorAdmin(admin.ModelAdmin):

    list_display = ( "name","image","rating")
    list_filter= ("rating",)

class ReviewAdmin (admin.ModelAdmin):

    list_display = ("user", "translator", "rating")
    list_filter = ("translator", "rating")


admin.site.register(Translator, TranslatorAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Language)
admin.site.register(specialty)