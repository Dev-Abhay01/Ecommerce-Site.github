from django.contrib import admin

# Register your models here.
from.models import *
class contactAdmin(admin.ModelAdmin):
    list_display=("name","contact","email","message")
admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=("cname","cimage","ADD_DATE")
admin.site.register(category,categoryAdmin)

class signupAdmin(admin.ModelAdmin):
    list_display=("name","DOB","gender","Mobile","email","password","profession","working","profile_picture")
admin.site.register(signup,signupAdmin)

class blogdetailAdmin(admin.ModelAdmin):
    list_display=("authorid","blogcategory","btitle","bdescription","battachment","bthumbnail","blogdate")
admin.site.register(blogdetail,blogdetailAdmin)