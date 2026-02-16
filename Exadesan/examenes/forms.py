from django import forms
from .models import CatalogoExamen
from .models import ResultadoExamen
from django.contrib.auth.models import User
from .models import Perfil




class CatalogoExamenForm(forms.ModelForm):
    class Meta:
        model = CatalogoExamen
        fields = ['nombre', 'unidad_medida', 'rango_min', 'rango_max', 'codigo_referencia']

        from django import forms
from .models import CatalogoExamen
class ResultadoExamenForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    examen_tipo = forms.ModelChoiceField(
        queryset=CatalogoExamen.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = ResultadoExamen
        fields = ['paciente', 'examen_tipo', 'fecha_examen', 'valor', 'documento_pdf']
        widgets = {
            'fecha_examen': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'documento_pdf': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': '.pdf,.jpg,.png'}),
        }

class UsuarioForm(forms.ModelForm):
    telefono = forms.CharField(required=False)
    rol = forms.ChoiceField(choices=Perfil.ROLES)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            Perfil.objects.create(
                usuario=user,
                telefono=self.cleaned_data.get("telefono"),
                rol=self.cleaned_data.get("rol"),
            )
        return user


