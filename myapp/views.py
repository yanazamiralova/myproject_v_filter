from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import Http404, HttpResponseNotFound
from .forms import SignUpForm, LoginForm, NewOrderForm
from .models import Orders, Status
from .filters import OrdersFilter

def index(request):
    filter = None
    try:
        if request.user.is_superuser:
            filter = OrdersFilter(request.GET, queryset=Orders.objects.order_by('id'))
        else:
            filter = OrdersFilter(request.GET, queryset=Orders.objects.filter(owner=request.user).order_by('id'))
    except Exception as e:
        orders = None
    return render(request, 'myapp/index.html', {'filter': filter})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем нового пользователя
            login(request, user)  # Выполняем вход
            return redirect('home')  # Перенаправляем на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'myapp/signup.html', {'form': form})


def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)  # Проверяем учетные данные
            if user is not None:
                login(request, user)  # Выполняем вход
                return redirect('home')  # Перенаправляем на главную страницу
    return render(request, 'myapp/login.html', {'form': form})


def set_orders(request):
    if request.method == 'POST':
        form = NewOrderForm(request.POST)
        form.instance.owner = request.user
        form.instance.status = Status.objects.get(title="новая заявка")
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            raise Http404
    else:
        form = NewOrderForm()
    return render(request, 'myapp/neworder.html', {'form': form})


# изменение данных в бд
def edit(request, id):
    try:
        order = Orders.objects.get(id=id)
        status = Status.objects.order_by('id')
        if request.method == "POST":
            print(request.POST)
            order.status_id = request.POST.get("status")
            order.save()
            return redirect("/")
        else:
            return render(request, "myapp/edit.html", {"order": order, "status": status})
    except Orders.DoesNotExist:
        return HttpResponseNotFound("<h2>Заявка не найдена!</h2>")
