# views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.decorators import login_required
from .models import UserInformation



@login_required
def user_information_form(request):
    # Check if user already has information
    user_info = UserInformation.objects.filter(user=request.user).first()
    if user_info:
        return redirect('user_information_display')

    if request.method == 'POST':
        try:
            # Validate data
            age = int(request.POST['age'])
            if age < 0 or age > 120:
                raise ValueError("Invalid age")

            height = float(request.POST['height'])
            if height < 0 or height > 300:
                raise ValueError("Invalid height")

            weight = float(request.POST['weight'])
            if weight < 0 or weight > 500:
                raise ValueError("Invalid weight")

            # Create user information
            user_info = UserInformation(
                user=request.user,
                age=age,
                gender=request.POST['gender'],
                height=height,
                weight=weight,
                fitness_goal=request.POST['fitness_goal'],
                medical_conditions=request.POST.get('medical_conditions', ''),
                phone=request.POST['phone'],
                address=request.POST['address']
            )
            user_info.save()
            
            messages.success(request, 'Your information has been saved successfully!')
            return redirect('user_information_display')

        except ValueError as e:
            messages.error(request, f'Invalid data: {str(e)}')
        except Exception as e:
            messages.error(request, f'Error saving information: {str(e)}')

    return render(request, 'user_information_form.html')

@login_required
def user_information_display(request):
    user_info = UserInformation.objects.filter(user=request.user).first()
    
    if not user_info:
        messages.warning(request, 'Please complete your information first.')
        return redirect('user_information_form')
    
    context = {
        'user_info': user_info,
        'bmi': user_info.calculate_bmi(),
        'bmi_category': user_info.get_bmi_category(),
        'user': request.user,
        'date_joined': request.user.date_joined,
    }
    return render(request, 'user_information_display.html', context)

@login_required
def user_information_edit(request):
    user_info = UserInformation.objects.filter(user=request.user).first()
    
    if not user_info:
        messages.warning(request, 'Please complete your information first.')
        return redirect('user_information_form')
    
    if request.method == 'POST':
        try:
            # Validate data
            age = int(request.POST['age'])
            if age < 0 or age > 120:
                raise ValueError("Invalid age")

            height = float(request.POST['height'])
            if height < 0 or height > 300:
                raise ValueError("Invalid height")

            weight = float(request.POST['weight'])
            if weight < 0 or weight > 500:
                raise ValueError("Invalid weight")

            # Update user information
            user_info.age = age
            user_info.gender = request.POST['gender']
            user_info.height = height
            user_info.weight = weight
            user_info.fitness_goal = request.POST['fitness_goal']
            user_info.medical_conditions = request.POST.get('medical_conditions', '')
            user_info.phone = request.POST['phone']
            user_info.address = request.POST['address']
            user_info.save()

            messages.success(request, 'Your information has been updated successfully!')
            return redirect('user_information_display')

        except ValueError as e:
            messages.error(request, f'Invalid data: {str(e)}')
        except Exception as e:
            messages.error(request, f'Error updating information: {str(e)}')

    context = {
        'user_info': user_info
    }
    return render(request, 'user_information_form.html', context)












def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')


def protinecal(request):
    return render(request, 'protinecal.html')

def contact(request):
    return render(request, 'contact.html')

def contactus(request):
    return render(request, 'contactus.html')

def article(request):
    return render(request, 'article.html')

def usertrainer(request):
    return render(request, 'usertrainer.html')

def gender(request):
    return render(request, 'Gender.html')

def bmi(request):
    return render(request, 'bmi.html')

def ashok(request):
    return render(request, 'ashok.html')

def rahul(request):
    return render(request, 'rahul.html')



def joinvideocall(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/videocall?roomID=" + roomID)
    return render(request, 'joinvideocall.html')





def blogs(request):
    # Retrieve all blog posts
    posts = Post.objects.filter(status=1)  # You might want to filter for published posts

    # Render the 'blogs.html' template with the posts data
    return render(request, 'blogs.html', {'posts': posts})



def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'myapp/post_detail.html', {'post': post})

def dashboard(request):
    # Ensure the user is authenticated before accessing dashboard
    if request.user.is_authenticated:
        user_name = request.user.first_name  # Get the logged-in user's first name
    else:
        return redirect('signin')  # If the user is not logged in, set to "Guest"
    
    # Render the dashboard page with the user's name
    return render(request, 'dashboard.html', {'name': user_name})

def videocallfun(request):
    # Ensure the user is authenticated before accessing dashboard
    if request.user.is_authenticated:
        user_name = request.user.first_name  # Get the logged-in user's first name
    else:
        return redirect('signin')  # If the user is not logged in, set to "Guest"
    
    # Render the dashboard page with the user's name
    return render(request, 'videocallfun.html', {'name': user_name})

def videocall(request):
    # Check if the user is authenticated before passing their name to the template
    if request.user.is_authenticated:
        user_name = request.user.first_name  # Get the logged-in user's first name
    else:
        return redirect('signin')  # If the user is not logged in, set to "Guest"
    
    return render(request, 'videocall.html', {'name': user_name})

# Add this to your existing views.py
def myaccount(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    
    context = {
        'user': request.user,
        'username': request.user.username,
        'first_name': request.user.first_name,
        'email': request.user.email,
        'date_joined': request.user.date_joined,
        'last_login': request.user.last_login
    }
    return render(request, 'myaccount.html', context)
    

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        fname = request.POST.get('fname', '').strip()
        email = request.POST.get('email', '').strip()
        pass1 = request.POST.get('pass1', '').strip()
        pass2 = request.POST.get('pass2', '').strip()

        # Server-side validation
        if not all([username, fname, email, pass1, pass2]):
            messages.error(request, "All fields are required.")
            return render(request, 'signup.html')

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        # Check password length
        if len(pass1) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return render(request, 'signup.html')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'signup.html')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'signup.html')

        try:
            # Create the user
            myuser = User.objects.create_user(username=username, email=email, password=pass1)
            myuser.first_name = fname
            myuser.save()

            messages.success(request, 'Your Account Has Been Successfully Created.')
            return redirect('signin')

        except Exception as e:
            messages.error(request, "An error occurred during registration.")
            return render(request, 'signup.html')

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        # Authenticate the user using the credentials
        user = authenticate(request, username=username, password=pass1)
        
        # If authentication is successful, login the user
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard page after successful login
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('signin')  # Redirect back to the sign-in page if authentication fails

    # For GET request, render the sign-in form
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    messages.success(request, "You logged out successfully.")
    return redirect('home')  # Redirect to home page after logging out
