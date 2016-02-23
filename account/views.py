from django.shortcuts import render ,render_to_response
from account.forms import UserForm 
from django.contrib.auth.decorators import login_required
# Create your views here
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse ,HttpRequest
from django.template import RequestContext
def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Vous etes la bienvenue"}
    return render_to_response('account/index.html', context_dict, context)
def about(request):
    
    context = RequestContext(request)
    context_dict = {'boldmessage': "Nous sommes ....."}
    return render_to_response('account/about.html', context_dict, context)
    
def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors 
    else:
        user_form = UserForm()
    return render_to_response(
            'account/register.html',
            {'user_form': user_form, 'registered': registered},
            context)

def user_login(request):
    
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user :  
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/account/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('account/login.html', {}, context)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/account/')
@login_required
def pid (request) :
    context = RequestContext(request)
    if request.method == 'GET':
        Process_name = request.GET.get('Process name')
        Process_pid = request.POST.get('Process pid')
  	
    return render_to_response(
            'account/process1.html',{},context)
