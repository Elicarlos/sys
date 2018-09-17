from django.contrib import admin
from .models import Cliente, Atendimento, Tecnico, Sistemas

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Atendimento)
admin.site.register(Tecnico)
admin.site.register(Sistemas)
