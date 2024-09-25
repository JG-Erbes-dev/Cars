from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 199999:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$ 200.000,00')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 2017:
           self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 2017')
        return factory_year