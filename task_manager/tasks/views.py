from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Task
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Task
from .forms import TaskForm
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Task
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import Task



from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import TaskSerializer


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

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Task.objects.all()
        title_contains = self.request.GET.get('title_contains')
        priority = self.request.GET.get('priority')
        is_complete = self.request.GET.get('is_complete')

        if title_contains:
            queryset = queryset.filter(title__icontains=title_contains)

        if priority:
            queryset = queryset.filter(priority=priority)

        if is_complete:
            is_complete = is_complete.lower() == 'true'
            queryset = queryset.filter(is_complete=is_complete)

        return queryset


        if query:
            return Task.objects.filter(title__icontains=query)
        else:
            return Task.objects.all()


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user to the task
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task-list')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    success_url = reverse_lazy('task-list')
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'due_date', 'photos', 'priority', 'is_complete']


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')



class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
