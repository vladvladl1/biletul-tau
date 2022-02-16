from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q
from accounts.forms import CreateUserForm
from accounts.models import Bilet, Eveniment


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('choose')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				auth.login(request, user)
				return redirect('choose')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def homePage(request):
	query = request.GET.get('numeev')
	if query!=None:
		events = Eveniment.objects.filter(Nume__icontains=query)
	else:

		events=Eveniment.objects.all()
	context = { 'events': events}
	return render(request, 'index.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def choosePage(request):
	context = {}
	return render(request, 'prima.html', context)

def adaugaEvent(request):
	if request.method == 'POST':
		id = request.POST['ID']
		nume = request.POST['Nume']
		descriere = request.POST['Descriere']
		artisti = request.POST['Artisti']
		oras = request.POST['Oras']
		pret = request.POST['Pret']
		data = request.POST['Data']
		categorie = request.POST['Categorie']
		var = Eveniment(ID=id,Nume=nume, Descriere=descriere,Artisti=artisti,Oras=oras,Pret=pret,Data=data,Categorie=categorie)
		var.save()

	context = {}
	return render(request, 'adaugaevent.html', context)

def cumparaBilet(request):
	context = {}
	return render(request, 'cumpara.html', context)


