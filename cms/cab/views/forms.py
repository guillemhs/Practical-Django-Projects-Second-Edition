from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from cms.cab.forms import SignupForm

def signup( request ):
    if request.method == 'POST':
        form = SignupForm( data = request.POST )
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect( "/accounts/login/" )
    else:
        form = SignupForm()
    return render_to_response( 'signup.html', { 'form': form } )

from django import forms
from cms.cab.models import Snippet, Language

class AddSnippetForm( forms.Form ):
    def __init__( self, author, *args, **kwargs ):
        super( AddSnippetForm, self ).__init__( *args, **kwargs )
        self.author = author

    title = forms.CharField( max_length = 255 )
    description = forms.CharField( widget = forms.Textarea() )
    code = forms.CharField( widget = forms.Textarea() )
    tags = forms.CharField( max_length = 255 )
    language = forms.ModelChoiceField( queryset = Language.objects.all() )

    def save( self ):
        return Snippet.objects.create( title = self.cleaned_data['title'],
                          description = self.cleaned_data['description'],
                          code = self.cleaned_data['code'],
                          tags = self.cleaned_data['tags'],
                          author = self.author,
                          language = self.cleaned_data['language'] )
