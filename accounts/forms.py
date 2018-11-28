from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class CustomCreationUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

#valdaremos que el email no exite para poder registrar el usuario
    def clean_email(self):
        #obtenemos el email que el usuario ingreso en el navegador
        email = self.cleaned_data['email']

        usuario = User.objects.filter(email=email)

        if usuario:
            #lanzamos una excepcion de validacion
            raise ValidationError("el email ya existe")


    class Meta:
        #le decimos al formulario que modelo utilizara para guardar los datos
        model = User

        fields = ('username','first_name','last_name','email','password1','password2')