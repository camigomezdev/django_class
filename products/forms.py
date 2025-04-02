
from django import forms


from .models import Comment


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = ('text', )

        widgets = {
            'text': forms.Textarea(attrs={
                'class': "form-control",
                'rows': "3",
                'placeholder': "Escribe tu comentario"
            })
        }
