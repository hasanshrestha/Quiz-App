from django import forms
from django.db.models import fields
from quizApp.models import AdminLogin, Question, User

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = AdminLogin
        fields = "username","password"
        labels = {
             "username": "",
             "password": ""
        } 
        widgets = {
            "username":  forms.TextInput(attrs={'placeholder':'Enter Username','autocomplete': 'off', 'class': 'form-control'}), 
            "password": forms.PasswordInput(attrs={'placeholder':'Enter Password','autocomplete': 'off','data-toggle': 'password', 'class': 'form-control'}),
        }

    # class CustomerLoginFrom(ModelForm):
    # class Meta:
    #     model = UserLogin
    #     fields = ['user_name','password']
    #     labels = {
    #         "user_name": "*Username",
    #         "password": "*Password"
    #     }    
    #     widgets = {
    #         "user_name":  TextInput(attrs={'placeholder':'ex:test','autocomplete': 'off'}), 
    #         "password": PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}),
    #     }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
        labels = {
             "question": "",
             "option1": "",
             "option2": "",
             "option3": "",
             "option4": "",
             "correctAns": "",
        }
        widgets = {
            "question":  forms.TextInput(attrs={'placeholder':'Enter Question','autocomplete': 'off', 'class': 'form-control'}),
            "option1":  forms.TextInput(attrs={'placeholder':'Enter Option One','autocomplete': 'off', 'class': 'form-control'}),
            "option2":  forms.TextInput(attrs={'placeholder':'Enter Option Two','autocomplete': 'off', 'class': 'form-control'}),
            "option3":  forms.TextInput(attrs={'placeholder':'Enter Option Three','autocomplete': 'off', 'class': 'form-control'}),
            "option4":  forms.TextInput(attrs={'placeholder':'Enter Option Four','autocomplete': 'off', 'class': 'form-control'}),
            "correctAns":  forms.TextInput(attrs={'placeholder':'Enter Correct Answer','autocomplete': 'off', 'class': 'form-control'})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        labels = {
             "username_user": "",
             "password_user": "",
             "firstname": "",
             "lastname": "",
             "password_user": "",
             "email": "",
             "contact": "",
             "image_url": "",
        }
        widgets = {
            "firstname":  forms.TextInput(attrs={'placeholder':'Enter First Name','autocomplete': 'off', 'class': 'form-control'}),
            "lastname":  forms.TextInput(attrs={'placeholder':'Enter Last Name','autocomplete': 'off', 'class': 'form-control'}),
            "username_user":  forms.TextInput(attrs={'placeholder':'Enter Username','autocomplete': 'off', 'class': 'form-control'}),
            "password_user": forms.PasswordInput(attrs={'placeholder':'Enter Password','autocomplete': 'off','data-toggle': 'password', 'class': 'form-control'}),
            "email":  forms.TextInput(attrs={'placeholder':'Enter Email Address','autocomplete': 'off', 'class': 'form-control'}),
            "contact":  forms.TextInput(attrs={'placeholder':'Enter Contact No.','autocomplete': 'off', 'class': 'form-control'}),
        }


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "username_user","password_user"
        labels = {
             "username_user": "",
             "password_user": ""
        }
        widgets = {
            "username_user":  forms.TextInput(attrs={'placeholder':'Enter Username','autocomplete': 'off', 'class': 'form-control'}), 
            "password_user": forms.PasswordInput(attrs={'placeholder':'Enter Password','autocomplete': 'off','data-toggle': 'password', 'class': 'form-control'}),
        }