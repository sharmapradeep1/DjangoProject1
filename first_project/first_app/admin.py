from django.contrib import admin

# Register your models here.
########## Pattern 5 STEP 30 connect to Database. Register models with admin so that the admin utility can be used for inserting databases


from first_app.models import AccessRecord, Webpage, Topic, User1, UserProfileInfo

admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(User1)
admin.site.register(UserProfileInfo)
