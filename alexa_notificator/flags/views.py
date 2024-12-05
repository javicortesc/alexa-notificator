from django.shortcuts import render, redirect
from .models import Flag
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import UserRegisterForm

# VITA DE REGISTER
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tu cuenta ha sido creada, {username}! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})



# VISTA PARA LAS FLAGS
@login_required
def flags_dashboard(request):
    # Obtener todas las flags del usuario logueado
    user_flags = Flag.objects.filter(user=request.user)
    
    if request.method == "POST":
        # Procesar cambios en las flags (activación/desactivación)
        for flag in user_flags:
            flag_status = request.POST.get(f"flag_{flag.id}")
            # Si la flag está activada, el checkbox estará marcado, de lo contrario no
            flag.is_active = (flag_status == 'on')  
            flag.save()

        return redirect('flags_dashboard')  # Redirige al panel de control después de guardar

    # Renderizar la plantilla con las flags del usuario
    return render(request, 'flags_dashboard.html', {'flags': user_flags})
