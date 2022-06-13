from . models import Share
from django import forms


class ShareForm(forms.ModelForm):

    class Meta:
        model = Share
        fields = ('target_user',)