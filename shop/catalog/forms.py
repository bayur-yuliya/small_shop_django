from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from catalog.models import Product, ProductCatalog


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username", required=True)
    email = forms.EmailField(label="Email address", required=True)
    password1 = forms.CharField(label="Password", required=True)
    password2 = forms.CharField(label="Password confirmation", required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CreateProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=ProductCatalog.objects.all(), initial=0)

    class Meta:
        model = Product
        fields = (
            "name",
            "category",
            "description",
            "price",
        )
