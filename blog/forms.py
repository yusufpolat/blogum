from django import forms

from .models import Post

class GonderiForm(forms.Form):
	class Meta:
		model = Post
		fields = ('baslik', 'yazi',)