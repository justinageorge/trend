from django import forms
from api.models import Category



class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=["name"]    

        widgets={"name":forms.TextInput(attrs={"class":"form-control"})}
