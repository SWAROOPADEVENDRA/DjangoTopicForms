from django import forms
from app.models import * 
class Topicforms(forms.Form):
    topic_name=forms.CharField(max_length=100)
    
class Webpageforms(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100)
    url=forms.URLField()
    
class Accessrecordforms(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    date=forms.DateField()
    author=forms.CharField()