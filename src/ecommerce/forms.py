from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "id":"form_full_name", "placeholder":"Your full name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "id":"form_email", "placeholder":"Your email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "id":"form_message", "placeholder":"Your message"}))

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())