from django import forms
from retailers.models import Items,Customers,Cart,Cart_contains,Orders


class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = "__all__"


class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = "__all__"


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"


class CartDetailsForm(forms.ModelForm):
    class Meta:
        model = Cart_contains
        fields = "__all__"


class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"