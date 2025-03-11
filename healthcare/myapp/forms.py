from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
        label=""
        )
    
    mobile = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
        label=""
        )

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
        label=""
        )
    
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}),
        label=""
        )
    
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'id': 'password'}),
        label=""
        )
    
    confirm_password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password', 'id': 'c_password'}),
        label=""
        )
    
    address = forms.CharField(
        max_length=100,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'style': 'height: 100px;'}),
        label=""
        )    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                field.widget.attrs['class'] += ' is-invalid'
            else:
                field.widget.attrs['class'] += ' is-valid'


    class Meta:
        model = User
        fields = ['username', 'mobile', 'email', 'age', 'password', 'confirm_password', 'address']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email
    
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit():
            raise forms.ValidationError("Mobile number must contain only digits.")
        if len(mobile) != 10:  # Adjust length as per requirements
            raise forms.ValidationError("Mobile number must be 10 digits long.")
        return mobile
    
    def clean_address(self):
        address = self.cleaned_data.get('address')
        if len(address.split()) < 3:  # Example: Require at least 3 words
            raise forms.ValidationError("Please enter a valid address.")
        return address

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
