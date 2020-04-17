from django.forms import ModelForm
from .models import Questions

class QuestionsModelForm(ModelForm):
    class Meta:
        model = Questions
        fields = "__all__"