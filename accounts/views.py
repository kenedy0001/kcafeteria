from pyexpat.errors import messages
from django.shortcuts import render, redirect
from accounts.forms import UserAdminCreationForm
from django.contrib.auth import logout,authenticate,login

def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(req, 'register.html', {'form': form})

def logoutUser(request):
	logout(request)
	return redirect('products')

def loginPage(request):

	if request.method == 'POST':
		phone = request.POST.get('phone')
		password =request.POST.get('password')

		user = authenticate(request, phone=phone, password=password)
		if user is not None:
			login(request, user)
			
			return redirect('products')
		else:
			# messages.info(request,'phone OR password is incorrect')
			return redirect('login')

	context = {}
	return render(request, 'registration/login.html', context)
