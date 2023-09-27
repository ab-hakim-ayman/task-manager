from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration.
            return redirect('task-list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task-list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


from django.shortcuts import render
from django.views.generic import ListView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Task
from .forms import TaskForm

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user to the task
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task-list')

from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Task

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import Task

class TaskUpdateView(UpdateView):
    model = Task
    success_url = reverse_lazy('task-list')
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'due_date', 'photos', 'priority', 'is_complete']

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Task

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
