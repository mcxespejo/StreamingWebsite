from django.contrib import admin
from .models import Movie, Geners, Banner, Side_items, Category, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Show the user linked to the profile in admin list view
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Geners)
admin.site.register(Banner)
admin.site.register(Side_items)

