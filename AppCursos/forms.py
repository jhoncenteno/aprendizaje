from django import forms
from AppCursos.models import Comentarios

class FormularioComentarios(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs = {  

        'class' : 'form-control',
        'placeholder' : 'Type your comment',
        'id' : 'comentariousuario',
        'rows' : '4'
    }))    

    class Meta:
        model = Comentarios     
        fields = ('content', )      