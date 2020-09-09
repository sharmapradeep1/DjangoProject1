from django import forms
from django.core import validators

from first_app.models import User1, UserProfileInfo #Forms 2, step 10 associate form to model

from django.contrib.auth.models import User

#Forms 1 - Use forms to capture data from screen, display it on console after some manual validations
#Forms 1 - Step 10 - create form class, similar to model

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to stary with z")

class form1_form(forms.Form):
    name = forms.CharField(validators=[check_for_z]) #validation option 4 - custom validation functions above form and use at field level
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea) # Widget text area aligns char field to html text area
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)]) #validation option 3 - default validators

    def clean(self): #validation option 1 - form level
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

#validation option 2 - function within form
    def clean_botcatcher(self): # On web page - inspect, navigate to hidden field, add attribute - value='20', add rest of fields and submit
        botcatcher = self.cleaned_data['botcatcher'] # as an alternate and better implementation, validator can be added to botcatcher field above
        if len(botcatcher) > 0:
            raise forms.ValidationError("Cought a bot")
        return botcatcher

#Forms 2, step 20 New form
class NewUserForm(forms.ModelForm):
    class Meta():
        model = User1
        fields = '__all__' # all fields from model. Optionally, inclusions / exclusions can be mentioned here


####Password 1 STEP 60 create forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
