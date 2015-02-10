from django import forms
from message_board import Message, Topic, Comment
from django.core.exceptions import ValidationError


class MessageForm(forms.ModelForm):
    message = forms.CharField(
        error_messages={"required": "Message field is required"},
        max_length=100, widget=forms.Textarea)
    topic = forms.ModelChoiceField(Topic.objects.all(), error_messages={
        "required": "Topic field is required"})

    def __init__(self, user=None, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        if user:
            self.user = user


    error_messages = {
        "invalid_message": "Message field is mandatory",
    }

    class Meta:
        model = Message
        exclude = ("creation_date", "last_modified", "user")
        fields = ("message", "topic",)

    def save(self, commit=True):
        message = Message(message=self.cleaned_data['message'], user=self.user,
                          topic=self.cleaned_data['topic'])
        if commit:
            message.save()
        return message


class CommentForm(forms.ModelForm):
    comment = forms.CharField(error_messages={"required": "Comment field is required"},
                              widget=forms.Textarea)

    def __init__(self, message, user=None, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.message = message
        if user:
            self.user = user

    class Meta:
        model = Comment
        fields = ("comment",)

    def save(self, commit=True):
        comment = Comment(comment=self.cleaned_data['comment'], user=self.user,
                          message=self.message)
        if comment:
            comment.save()
        return comment


