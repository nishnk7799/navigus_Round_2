from django import forms
from .models import Post

class HomeForm(forms.ModelForm):
    Document=forms.CharField(label=False,widget=forms.Textarea(attrs={'height':"100%","rows":250, "cols":90,'style':'height: 450px;width: 750px;'}))
    class Meta:
        model=Post
        fields = ('Document',)

