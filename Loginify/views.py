from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import UserDetails
from django.core.serializers import serialize

# Create your views here.

def hello(request):
    return HttpResponse("Hello, Wordl!!!")

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if UserDetails.objects.filter(email=email).exists():
            return HttpResponse("email already exists!")
        
        user = UserDetails(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request,'signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserDetails.objects.get(email=email, password=password)
            return HttpResponse(f"Welcome, {user.username}")
        except UserDetails.DoesNotExist:
            return HttpResponse("Invalid email or password!")
    return render(request, 'login.html')

def create_user_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if UserDetails.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)  # Error response
        
        user = UserDetails.objects.create(username=username, email=email, password=password)
        return JsonResponse({'message': 'User created successfully!', 'user': {'username': user.username, 'email': user.email}}, status=201)
    return JsonResponse({'error': 'GET method not allowed'}, status=405)

def getAllUsers_view(request):
    users = UserDetails.objects.all()
    userList = [{'username': user.username, 'email': user.email} for user in users]
    # usersJson = serialize('json', users)
    return JsonResponse(userList, safe=False)

def getSingleUser_view(request, username):
    try:
        user = UserDetails.objects.get(username=username)
        return JsonResponse({'username': user.username, 'email': user.email})
    except UserDetails.DoesNotExist:
        return HttpResponse("User not found!")
    
def updateUser_view(request, username):
    try:
        user = UserDetails.objects.get(username = username)
        if request.method == 'POST':
            user.email = request.POST['email']
            user.password = request.POST['password']
            user.save()
            return JsonResponse({'message': 'User updated successfully!', 'user': {'username': user.username, 'email': user.email}})
        return JsonResponse({'error': 'GET method not allowed'}, status=405)
    except UserDetails.DoesNotExist:
        return HttpResponse("User not found!")
    
def deleteUser_view(request, username):
    try:
        user = UserDetails.objects.get(username = username)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully!'})
    except UserDetails.DoesNotExist:
        return HttpResponse("User not found!")

