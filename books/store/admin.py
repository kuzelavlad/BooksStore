from django.contrib import admin
from .models import Books




#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ["username",]


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_filter = ["price", "date", "status", "category"]
    list_display = ["title", "author", "price", "status"]