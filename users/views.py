from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
	"""Регестрирует нового пользователя."""
	if request.method != 'POST':
		# Выводит пустую форму регестрации
		print("G")
		form = UserCreationForm()
	else:
		# Обработка заполненой формы
		form = UserCreationForm(data = request.POST)

		if form.is_valid():
			new_user = form.save()
			# Выполнить входи и перенаправить на домашнюю страеицу
			login(request,new_user)
			return redirect('learning_logs:index')

	# Вывести пустую или недействительную форму
	context = {'form':form}
	return render(request, 'registration/register.html', context)