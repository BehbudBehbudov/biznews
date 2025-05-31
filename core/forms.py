from django import forms
from core.models import ContactUs, NewsletterSubscription, Comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name',  'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınızı daxil edin.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email-i daxil edin.'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mövzu xətti.'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınızı yazın', 'rows': 4}),
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ["email"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'website', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name *'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email *'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Your Website'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment *', 'rows': 5}),
        }
