from django.contrib import admin
from .models import *
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','image']
class BillAdmin(admin.ModelAdmin):
    list_display = ['name','email','address','city','state','zip','name_on_card','cardno','expmonth','expyear']
class TableAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','date_table','time_table','category','msg']
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'cpassword']
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'mailid', 'service','food','cleanliness','ResponseTime','recommend','rating']
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','city','query']
class CaterAdmin(admin.ModelAdmin):
    list_display = ['cid','name','dcategory','dcapacity','dicategory','dicapacity','tcategory','tcapacity','pcategory','pcapacity','rcategory','rcapacity','decategory','decapacity','drcategory','drcapacity','maincategory','maincapacity']
admin.site.register(items,ItemAdmin)
admin.site.register(User_module,UserAdmin)
admin.site.register(storeItem)
admin.site.register(bills,BillAdmin)
admin.site.register(book_table,TableAdmin)
admin.site.register(Query_table)
admin.site.register(Feedback_form,FeedbackAdmin)
admin.site.register(Contact_details,ContactAdmin)
admin.site.register(ritem)
admin.site.register(recommendations)
admin.site.register(orders)

