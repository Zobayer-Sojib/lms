from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Q

from .forms import NewUserForm
from django.contrib.auth import login

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, authenticate, logout

from .models import book,BookDB




def search(request):
    error=""
    if request.method == 'GET':
        query = request.GET.get('search')
    if query:
        queryset = (Q(book_name__icontains=query)) | (Q(book_writer__icontains=query)) | (Q(publisher__icontains=query)) | (Q(book_id__icontains=query))
        results = book.objects.filter(queryset).distinct()

    else:
        results=[]
    if not results:
        error=" not found"

    context = {
        'results':results,
        "error":error
    }
    return render(request, 'search.html', context)

    
    
def index(request):
    return render(request, 'index.html')

def show(request):
    show_data = book.objects.all()
    return render(request, 'showdata.html', {'showdata': show_data} )


def searchhistory(request):
    return render(request, 'searchhistory.html' )


def addinfo(request):
    if request.method == 'POST':
        
        boname =request.POST.get('bname')
        bowriter =request.POST.get('bWriter')
        bopublisher =request.POST.get('bPublisher')
        boid =request.POST.get('bid')

        adddata = book(book_name=boname, book_writer=bowriter, publisher=bopublisher, book_id=boid )
        adddata.save()
        messages.success(request, 'successfully added')
      
    return render(request, 'insertData.html')


def editinfondelete(request):
     updatedata = book.objects.all()
     contex = {'updateinfo':updatedata}
     return render(request, 'updatendelete.html',contex )



def edit(request, id):
    edit = book.objects.get(pk=id)
    contex={'edit':edit}
    return render(request, 'edit.html', contex)

def update(request, id):
    edit = book.objects.get(pk=id)
    edit.book_name = request.GET['bn']
    edit.book_writer = request.GET['bw']
    edit.publisher = request.GET['bp']
    edit.save()
    return redirect('editndel')
    


def delete(request, id):
    remove = book.objects.get(pk=id)
    remove.delete()
    return redirect('editndel')





def bookList(request):
    BList= BookDB.objects.all()
    return render(request, 'BookList.html', {'Blist':BList})



def order(request):
    return render(request, 'order.html')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, 'register.html', context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("next")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"login.html", context={"login_form":form})


def next(request):
    return render(request, 'next.html')


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")