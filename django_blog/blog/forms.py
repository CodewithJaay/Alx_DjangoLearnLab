from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Add tags separated by commas",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Django, Python, WebDev"})
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter post title"}),
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Write your content here..."}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # Handle tags
        tags_str = self.cleaned_data.get("tags", "")
        if tags_str:
            tag_names = [tag.strip() for tag in tags_str.split(",") if tag.strip()]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)
        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Write your comment here..."}),
        }

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content or content.strip() == "":
            raise forms.ValidationError("Comment cannot be empty.")
        if len(content) < 3:
            raise forms.ValidationError("Comment must be at least 3 characters long.")
        return content
