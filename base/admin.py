from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Company)
admin.site.register(PersonGame)
admin.site.register(Game)
admin.site.register(GameShorts)
admin.site.register(Review)
