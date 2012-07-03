from django import forms
from django.contrib.auth.models import User

class SignupForm( forms.Form ):

    username = forms.CharField( max_length = 30 )
    email = forms.EmailField()
    password1 = forms.CharField( max_length = 30, widget = forms.PasswordInput( render_value = False ) )
    password2 = forms.CharField( max_length = 30, widget = forms.PasswordInput( render_value = False ) )

    def clean_username( self ):
        try:
            User.objects.get( username = self.cleaned_data['username'] )
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError( "This username is already in use. Please choose another." )

    def clean( self ):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError( "You must type the same password each time" )
        return self.cleaned_data

    def save( self ):
        new_user = User.objects.create_user( username = self.cleaned_data['username'], email = self.cleaned_data['email'], password = self.cleaned_data['password1'] )
        return new_user




# Not needed.

# from django import forms
# from cab.models import Snippet, Language
# 
# class AddSnippetForm(forms.Form):
#     def __init__(self, author, *args, **kwargs):
#         super(AddSnippetForm, self).__init__(*args, **kwargs)
#         self.author = author
# 
#     title = forms.CharField(max_length=255)
#     description = forms.CharField(widget=forms.Textarea())
#     code = forms.CharField(widget=forms.Textarea())
#     tags = forms.CharField(max_length=255)
#     language = forms.ModelChoiceField(queryset=Language.objects.all())
#     
#     def save(self):
#         return Snippet.objects.create(title=self.cleaned_data['title'],
#                           description=self.cleaned_data['description'],
#                           code=self.cleaned_data['code'],
#                           tags=self.cleaned_data['tags'],
#                           author=self.author,
#                           language=self.cleaned_data['language'])
