from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    
    def save(self, *args, **kwargs):
        self.nome = self.nome.title()
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
