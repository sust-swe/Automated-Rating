from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        #login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')

            # for login required funcionality
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else :
                return redirect('dashboard')
        else:
            messages.error(request, 'Login Failed ! Credential Error !')
            return redirect('login')
    else :
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        #get Form variable
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check validation
        if password == password2:
            #check existing username
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Username is already Taken !')
                return redirect('register')
            else:
                #check existing email
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'Email is registered Before !')
                    return redirect('register')
                else :
                    #Everything is okay
                    user = User.objects.create_user(username = username, password = password, email = email,
                    first_name = first_name, last_name = last_name)

                    #auto login after register
                    #auth.login(request, user)
                    #messages.success(request, 'You are logged in')
                    #return redirect('index')

                    #do login after register
                    user.save()
                    return redirect('login')
        else:
            messages.error(request, 'Password Do Not Match !')
            return redirect('register')
    else :
        return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        #messages.success(request, "You are now Logged out !")
        auth.logout(request)
        return redirect('index')


def dashboard(request):
    #user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    #context = {
    #    'contacts' : user_contacts
    #}

    return render(request, 'accounts/dashboard.html')