from django.forms import ModelForm

from .models import LoadImage

class ImageForm(ModelForm):
    class Meta:
        model = LoadImage
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image'].widget.attrs.update({'id': 'birthdayDate'})