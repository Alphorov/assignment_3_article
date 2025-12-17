# forms.py
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body"]

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter article title",
                "maxlength": "25",
            }
        ),
        label="Article Title",
        help_text="Maximum 25 characters",
    )

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write your article content here...",
                "maxlength": "100",
            }
        ),
        label="Article Content",
    )
