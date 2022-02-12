from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  get_user_model
from django.urls import reverse_lazy
from django.conf import settings
from django import forms
from .models import Article

User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password1","password2")


    def save(self,commit=True):
        #user= super().save(commit=False)
        #user.email=self.cleaned_data["email"]
        user.save()
        return user

class ArticleCreateForm(forms.ModelForm): # DjangoのModelFormでは強力なValidationを使える
    class Meta:
        model = Article # Article モデルと接続し、Article モデルの内容に応じてformを作ってくれる
        fields = ('title', 'text') # 入力するカラムを指定
