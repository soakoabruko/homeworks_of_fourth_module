from django import forms
from .models import Advertisment
from django.core.exceptions import ValidationError

class AdvertismentForm( forms.ModelForm ):
    class Meta:
        model = Advertisment
        fields = [ 'title', 'description', 'price', 'auction', 'image' ]
        widgets = { 'title' : forms.TextInput( attrs = { 'class': 'form-control form-control-lg' } ),
                                                       'description' : forms.Textarea( attrs = { 'class' : 'form-control form-control-lg' } ),
                                                        'price' : forms.NumberInput( attrs = { 'class' : 'form-control form-control-lg' } ),
                                                        'auction' : forms.CheckboxInput( attrs = { 'class': 'format-check-input' } ),
                                                        'image' : forms.FileInput( attrs = { 'class' : 'form-control form-control-lg' } ) }
    
    def clean_title( self ):
        title = self.cleaned_data[ 'title' ]
        if title.startswith( '?' ):
            raise ValidationError( 'Заголовок не может начинаться с вопросительного знака.' )
        return title