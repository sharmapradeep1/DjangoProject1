from django.shortcuts import render
from django.http import HttpResponse

########## Pattern 5 STEP 60, display values from DB, import Models in viewa
from first_app.models import Topic,Webpage,AccessRecord,User1

#Forms 1 - Step 20 - create views for form
from first_app import forms


# Create your views here.
# Views along with urls help to render / diaplay
# Templates help in managing / displaying static information
# Model helps in getting dynamic information from DB


###########Password 1 STEP 80 create views
from first_app.forms import UserForm,UserProfileInfoForm



# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
    return render(request,'first_app/index.html',context=my_dict)

########## Pattern 1 STEP 30 Manage url in project - if http://127.0.0.1:8000/home, invoke home function in app - views
def home1(request):
    return HttpResponse("<B>Pattern 1 : URL managed in Project, view in application !</B>")

########## Pattern 2 STEP 50 Manage url in app - if http://127.0.0.1:8000/first_app/home2, call hoem2 in app-> views
def home2(request):
    return HttpResponse("<B>Pattern 2 : URL managed in app, view in application !</B>")

########## Pattern 3 STEP 40 Render page instead of http response url in app - http://127.0.0.1:8000/first_app/home3, call home3 in app-> views
def home3(request):
    tempdict = {'temp_insert':'Pattern 3 : I am Text from Dictionary into HTML Template', 'temp_num':111}
    return render(request,'first_app/renderTemplate.html',context=tempdict)

########## Pattern 4 STEP 50 Render page, associate static content
def home4(request):
    temp2dict = {'temp2_insert':"Now I am coming from first_app/displayStatic.html!"}
    #return HttpResponse("<B>Pattern 1 : URL managed in Project, view in application !</B>")
    return render(request,'first_app/displayStatic.html',context=temp2dict)


########## Pattern 5 STEP 70, display values from DB, associate db content with template
def home5(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,'first_app/displaydatabase.html',date_dict)

########## Pattern 5 , users
def home5b(request):
    user_list = User1.objects.order_by('first_name')
    user_dict = {"user_records":user_list}
    return render(request,'first_app/displayusers.html',context=user_dict)


#Forms 1 - Step 30 - create views for form

@login_required
def form1_view(request):
    form = forms.form1_form() #If only form1_form was imported above, no need of 'forms.' here

    if request.method == 'POST':
        form = forms.form1_form(request.POST) #If request is to submit details from screen

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request,'first_app/form1_template.html',{'form':form}) #If request is to render form initially



#Forms 2, step 30 New view
@login_required
def NewUserView(request):

    form = forms.NewUserForm()

    if request.method == "POST":
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True) #If post and form is valid, commit to DB
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'first_app/NewUserHTML.html',{'form':form}) #New page - oprn html




###########Password 1 STEP 80 create views

# Create your views here.

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user
            print(profile.user, profile.portfolio_site)
            print(user.username, user.password)
            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'first_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'first_app/login.html', {})
