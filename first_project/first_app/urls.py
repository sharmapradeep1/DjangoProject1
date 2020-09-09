from django.conf.urls import url
from first_app import views ########## Pattern 2 STEP 30 Manage url in app - projects url redirected here as http://127.0.0.1:8000/first_app

##### Pattern 11 Step 10, relative paths for pages and template inheritence  SET THE NAMESPACE!
app_name = 'first_app'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^home2/',views.home2,name='home2'), ########## Pattern 2 STEP 40 Manage url in app - if http://127.0.0.1:8000/first_app/home2, call home2 in app-> views
    #Only home2 above and not first_app/home2 as the search path from projects url is ^first_app/ ^home2/ [name='home2']
    url(r'^home3/',views.home3,name='home3'),
    ########## Pattern 3 STEP 10 Render page instead of http response url in app - http://127.0.0.1:8000/first_app/home3, call home3 in app-> views
    url(r'^home4/',views.home4,name='home4'),
    ########## Pattern 4 STEP 40 Render page, associate static content
    url(r'^home5/',views.home5,name='home5'),
    url(r'^home5b/',views.home5b,name='home5b'),
    ########## Pattern 5 STEP 90 Render page, associate db content
    url(r'^form1/',views.form1_view,name='form1_form'),
    #Forms 1 - Step 40 - first_app/form1 url navigasted to form1_view
    url(r'^form2/',views.NewUserView,name='form2_form'),
    #Forms 2 - Step 40 - first_app/form2 url navigasted to NewUserView
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    ############Password 1 STEP 90 create urls
]
