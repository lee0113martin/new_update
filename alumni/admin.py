from django.contrib import admin
from .models import alumni_tb, dzolali, leased, books

# Register your models here.

# 1. admin.site.register(alumni_tb)
# 2. admin.site.register(ITEMS)

@admin.register(alumni_tb)
class alumni_tbAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "team_name", "points_scored")

@admin.register(dzolali)
class dzolaliAdmin(admin.ModelAdmin):
    list_display = ("Item_Name", "Brand_Name", "Quantity", "Remark")

@admin.register(leased)
class leasedAdmin(admin.ModelAdmin):
    list_display = ("Item_Name", "Brand_Name", "Recipient", "Department", "Quantity", "Receive_Date", "Return_Date", "Remark")

@admin.register(books)
class booksAdmin(admin.ModelAdmin):
    list_display = ("Title", "Author", "Quantity", "Remark")