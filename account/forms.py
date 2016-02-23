from account.models import UserProfile
from django.contrib.auth.models import User
from django import forms

#from .app.account.models import MyModel
#from .apps.djangular.forms import NgFormValidationMixin, NgModelFormMixin, AddPlaceholderFormMixin
 
#class MyModelForm(NgModelFormMixin, forms.ModelForm):
 #    """
  #   mymodel Form with a little crispy forms added! 
   #  """
    # def __init__(self, *args, **kwargs):
         #super(MyModelForm, self).__init__(*args, **kwargs)
        # setup_bootstrap_helpers(self)
 
    # class Meta:
     #    model = MyModel
      #   fields = ('name', 'description',)
 
 #def setup_bootstrap_helpers(object):
  #   object.helper = FormHelper()
   #  object.helper.form_class = 'form-horizontal'
    # object.helper.label_class = 'col-lg-3'
    # object.helper.field_class = 'col-lg-8'
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
