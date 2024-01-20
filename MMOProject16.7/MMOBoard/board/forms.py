from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db.models import TextField
from django.forms import ModelForm, ChoiceField, CharField

from .models import Post, Reply, CATEGORIES


class PostForm(ModelForm):

    category = ChoiceField(
        choices=CATEGORIES,
        label='Select category',
        help_text='Required field.',
        error_messages={
            'required': 'You need to select one category!',
        }
    )

    title = CharField(
        min_length=1,
        label='Title',
        help_text='Required field. At least 1 symbol.',
        error_messages={
            'required': 'You need to add something!',
        }
    )

    content = CharField(
        widget=CKEditorUploadingWidget(),
        label='Content of post',
        required=False,
        help_text='Could be empty.',
    )

    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'content',
        ]


class ReplyForm(ModelForm):

    text = TextField()

    class Meta:
        model = Reply
        fields = [
            'text',
        ]
