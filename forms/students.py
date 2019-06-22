from onlineapp.models import *
from django.forms import *


class addcollege(ModelForm):
    class Meta:
        model =College
        exclude = ['id']
        widgets={
            'name' : TextInput(attrs={'class':'input is-info','placeholder':'Enter Name'}),
            'location' : TextInput(attrs={'class':'input is-info','placeholder':'Enter Location'}),
            'acronym' : TextInput(attrs={'class':'input is-info','placeholder':'Enter Acronym'}),
            'contact' : EmailInput(attrs={'class':'input is-info','placeholder':'Enter Contact'})
        }

class addstudent(ModelForm):
    class Meta:
        model=Student
        exclude=['id','dob','college']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Enter Name'}),
            'email': TextInput(attrs={'placeholder': 'Enter Email'}),
            'db_folder': TextInput(attrs={'placeholder': 'Enter db_folder_name'}),
            'dropped_out':CheckboxInput(),
        }

class addmocktest(ModelForm):
    class Meta:
        model=MockTest1
        exclude=['student','id']
        widgets={
            'problem1' : NumberInput(attrs={'placeholder': 'Score in problem 1'}),
            'problem2' : NumberInput(attrs={'placeholder': 'Score in problem 2'}),
            'problem3' : NumberInput(attrs={'placeholder': 'Score in problem 3'}),
            'problem4' : NumberInput(attrs={'placeholder': 'Score in problem 4'}),
            'total':NumberInput(attrs={'placeholder': '4'}),
        }


class loginn(Form):
    username=CharField(label='username',widget=TextInput(attrs={'placeholder':'enter username'}))
    password = CharField(label='password', widget=PasswordInput(attrs={'placeholder': 'enter password'}))

class signup(Form):
    username = CharField(label='username', widget=TextInput(attrs={'placeholder': 'enter username'}))
    password = CharField(label='password', widget=PasswordInput(attrs={'placeholder': 'enter password'}))
    first_name = CharField(label='firstname', widget=TextInput(attrs={'placeholder': 'enter first name'}))
    last_name = CharField(label='lastname', widget=TextInput(attrs={'placeholder': 'enter last name'}))