from django import forms
from .models import ContactForm,Flan

class FlanFormModel(forms.ModelForm):
    class Meta:
        model = Flan
        fields = ['name','description','image_url']

class MiForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Clave')



class ContactFormForm(forms.ModelForm):
    class Meta:
        model= ContactForm
        fields= ['customer_email','customer_name','message']

        labels={
            'customer_email':'Email',
            'customer_name':'Nombre',
            'message':'Mensaje',
        
        }

        widgets={
            'customer_email': forms.EmailInput(attrs={'class':'form-control'}),
            'customer_name': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.TextInput(attrs={'class':'form-control'}),
        }

class ContactForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')