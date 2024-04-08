from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length = 100)
    uf = models.CharField(max_length = 100)

    def __str__(self):
        return f" {self.nome} {self.uf}"
    class Meta:
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Ocupações"
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=100 )
    pai = models.CharField(max_length=100 )
    mae = models.CharField(max_length=100 )
    cpf = models.CharField(max_length=14)
    data_nasc = models.CharField(max_length=100 )
    email = models.CharField(max_length=100 )
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete = models.CASCADE)
    
    def __str__(self):
        return f" {self.nome} {self.pai} {self.mae} {self.cpf} {self.data_nasc} {self.email} {self.cidade} {self.ocupacao}"
    class Meta:
        verbose_name_plural = "Pessoas"


class Instituicao(models.Model):
    nome = models.CharField(max_length = 100)
    site = models.CharField(max_length = 100)
    telefone = models.CharField(max_length = 100)
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)

    def __str__(self):
        return f" {self.nome} {self.site} {self.telefone} {self.cidade}"
    class Meta:
        verbose_name_plural = "Instituições"
    
class Area(models.Model):
    nome = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Areas"
    
    
class Curso(models.Model):
    nome = models.CharField(max_length = 100)
    carga_horaria_total = models.CharField (max_length = 100)
    duracao_meses = models.CharField(max_length = 100)
    areas = models.ForeignKey(Area, on_delete  = models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete  = models.CASCADE)
    
    def __str__(self):
        return f" {self.nome} {self.carga_horaria_total} {self.duracao_meses} {self.areas} {self.instituicao}"
    class Meta:
        verbose_name_plural = "Cursos"
        
class Periodo(models.Model):
    nome = models.CharField(max_length = 100)
   
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Periodos"
        
class Disciplina(models.Model):
    nome = models.CharField(max_length = 100)
    areas = models.ForeignKey(Area, on_delete  = models.CASCADE)

    def __str__(self):
        return f" {self.nome} {self.areas}"
    class Meta:
        verbose_name_plural = "Disciplinas"
    
class Matricula (models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete = models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()
    
    def __str__(self):
        return f" {self.instituicao} {self.curso} {self.pessoa} {self.data_inicio} {self.data_previsao_termino}"
    class Meta:
        verbose_name_plural = "Matriculas"
    
class Avaliacao(models.Model):
    descricao = models.CharField(max_length = 100)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)

    def __str__(self):
        return f" {self.descricao} {self.curso} {self.disciplina}"
    class Meta:
        verbose_name_plural = "Avaliacoes"

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE)
    numero_faltas = models.CharField(max_length = 100)
    
    def __str__(self):
        return f" {self.curso} {self.disciplina} {self.pessoa} {self.numero_faltas}"
    class Meta:
        verbose_name_plural = "Frequencias"
    
class Turma(models.Model):
    nome = models.CharField(max_length = 100)
    turno = models.CharField(max_length = 100)
    
    def __str__(self):
        return f" {self.nome} {self.turno}"
    class Meta:
        verbose_name_plural = "Turmas"
    
class Ocorrencia(models.Model):
    descricao = models.CharField (max_length = 1000)
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE)
    
    def __str__(self):
        return f" {self.descricao} {self.data} {self.curso} {self.disciplina} {self.pessoa}"
    class Meta:
        verbose_name_plural = "Ocorrencias"

class Disciplina_curso(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)
    carga_horaria = models.CharField (max_length = 100)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete = models.CASCADE)
    
    def __str__(self):
        return f" {self.curso} {self.disciplina} {self.carga_horaria} {self.periodo}"
            
class Tipos_avaliacao(models.Model):
    nome = models.CharField(max_length = 100)
    
    def __str__ (self):
        return self.nome