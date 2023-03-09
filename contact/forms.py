from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class':'text-input-half-width', 'placeholder':'Name *'}))
	from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'text-input-half-width', 'placeholder':'Your E-mail *'}))
	subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'text-input-full-width', 'placeholder':'Subject *'}))
	message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'text-input-full-width', 'placeholder':'Message *'}))