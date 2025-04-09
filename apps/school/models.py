from django.db import models
from django.urls import reverse_lazy


class ClassGroup(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="nome da turma"
    )
    year = models.PositiveIntegerField(
        verbose_name="ano"
    )

    class Meta:
        verbose_name = "turma"
        verbose_name_plural = "turmas"

    def __str__(self):
        return f"{self.name} ({self.year})"


class Student(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="nome do aluno"
    )
    class_group = models.ForeignKey(
        ClassGroup,
        on_delete=models.CASCADE,
        verbose_name="turma",
        related_name='students',
    )
    color = models.CharField('cor', max_length=7, null=True, blank=True)
    phone = models.CharField('telefone', max_length=19, null=True, blank=True)

    class Meta:
        verbose_name = "aluno"
        verbose_name_plural = "alunos"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('school:student_list')


class Teacher(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="nome do professor"
    )

    class Meta:
        verbose_name = "professor"
        verbose_name_plural = "professores"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    date = models.DateField(
        verbose_name="data"
    )
    time = models.CharField(
        max_length=20,
        verbose_name="horário"
    )
    class_group = models.ForeignKey(
        ClassGroup,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name="turma"
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name="professor"
    )

    class Meta:
        verbose_name = "aula"
        verbose_name_plural = "aulas"

    def __str__(self):
        return f"Aula em {self.date} às {self.time} - {self.class_group.name}"


class Attendance(models.Model):
    pk = models.CompositePrimaryKey('student', 'date_attendance', 'lesson')
    date_attendance = models.DateField(auto_now_add=True, help_text='data da presença')
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendances',
        verbose_name="aluno"
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='attendances',
        verbose_name="aula"
    )
    present = models.BooleanField(
        default=False,
        verbose_name="presente"
    )
    note = models.TextField(
        blank=True,
        verbose_name="observação"
    )

    class Meta:
        verbose_name = "presença"
        verbose_name_plural = "presenças"

    def __str__(self):
        return f"{self.student.name} - {self.lesson} ({'Presente' if self.present else 'Faltou'})"

    def to_dict(self):
        return {
            'pk': self.pk,
            'display': f"{self.student.name} - {self.date_attendance} - {self.lesson.id}",
            'date_attendance': self.date_attendance,
            'student': self.student,
            'lesson': self.lesson,
            'present': self.present,
            'note': self.note,
        }
