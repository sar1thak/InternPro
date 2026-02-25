from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Task, Internship
from datetime import date
from django.core.mail import send_mail


# ================= SIGNUP =================
def signup_view(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/dashboard')

    return render(request, 'dashboard/signup.html', {'form': form})


# ================= LOGIN =================
def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/dashboard')

    return render(request, 'dashboard/login.html', {'form': form})


# ================= LOGOUT =================
def logout_view(request):
    logout(request)
    return redirect('/login')


# ================= DASHBOARD =================
def dashboard_home(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    # Fetch data
    tasks = Task.objects.filter(user=request.user).order_by('deadline')
    internships = Internship.objects.filter(user=request.user)

    # ===== SMART PRIORITY LOGIC =====
    today = date.today()
    urgent_tasks = []
    normal_tasks = []

    for task in tasks:
        days_left = (task.deadline - today).days

    
        if days_left == 1:
            send_mail(
                subject='Task Deadline Reminder',
                message=f'Your task "{task.title}" deadline is tomorrow!',
                from_email='noreply@internmanager.com',
                recipient_list=[request.user.email],
                fail_silently=True,
            )

        if days_left <= 2:
            urgent_tasks.append(task)
        else:
            normal_tasks.append(task)

    # ===== ADD TASK / INTERNSHIP =====
    if request.method == "POST":

        # Add Task
        if "task_submit" in request.POST:
            title = request.POST.get("title")
            deadline = request.POST.get("deadline")
            priority = request.POST.get("priority")

            Task.objects.create(
                user=request.user,
                title=title,
                deadline=deadline,
                priority=priority
            )
            return redirect('/dashboard')

        # Add Internship
        if "intern_submit" in request.POST:
            company = request.POST.get("company")
            role = request.POST.get("role")
            status = request.POST.get("status")

            Internship.objects.create(
                user=request.user,
                company=company,
                role=role,
                status=status
            )
            return redirect('/dashboard')
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = total_tasks - completed_tasks
    
    total_internships = internships.count()
    # ===== AI SUGGESTION ENGINE =====
    ai_message = ""

    if pending_tasks > 5:
        ai_message = "You have many pending tasks. Focus on high priority items first."
    elif total_internships == 0:
        ai_message = "No internships applied yet. Start applying today."
    elif completed_tasks > pending_tasks:
        ai_message = "Great productivity! Keep going."
    else:
        ai_message = "Stay consistent and complete pending tasks."

    context = {
        "urgent_tasks": urgent_tasks,
        "normal_tasks": normal_tasks,
        "internships": internships,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "total_internships": total_internships,
        "ai_message": ai_message,
    }

    return render(request, "dashboard/dashboard.html", context)

def analytics_page(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    tasks = Task.objects.filter(user=request.user)
    internships = Internship.objects.filter(user=request.user)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = total_tasks - completed_tasks

    high_priority = tasks.filter(priority="High").count()
    medium_priority = tasks.filter(priority="Medium").count()
    low_priority = tasks.filter(priority="Low").count()

    context = {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "total_internships": internships.count(),
        "high_priority": high_priority,
        "medium_priority": medium_priority,
        "low_priority": low_priority,
    }

    return render(request, "dashboard/analytics.html", context)

def complete_task(request, task_id):
    if not request.user.is_authenticated:
        return redirect('/login')

    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = True
    task.save()

    return redirect('/dashboard')

def delete_task(request, task_id):
    if not request.user.is_authenticated:
        return redirect('/login')

    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('/dashboard')

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.priority = request.POST.get("priority")
        task.save()
        return redirect('/dashboard')

    return render(request, "dashboard/edit.html", {"task": task})