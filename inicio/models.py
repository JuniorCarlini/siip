from django.db import models

class Proprietario(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='proprietarios/', null=True, blank=True)
    numero_telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Propriedade(models.Model):
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE, related_name='propriedades')
    nome_propriedade = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    def __str__(self):
        return self.nome_propriedade

class Armadilha(models.Model):
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE, related_name='armadilhas')
    identificador = models.CharField(max_length=50)
    coordenadas_geograficas = models.CharField(max_length=50)  # ou use um campo específico para coordenadas geográficas
    horario_ultima_sincronizacao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.identificador
