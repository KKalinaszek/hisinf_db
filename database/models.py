from django.db import models
from django.contrib.auth import get_user_model

PAGE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
    )

# 1
class Board(models.Model):
    id = models.AutoField(primary_key=True)
    no = models.PositiveIntegerField(default=0)
    page = models.CharField(max_length=1, choices=PAGE_CHOICES)
    title = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Boards'
        unique_together = ('no', 'page')

# 2
class Section(models.Model):
    id = models.AutoField(primary_key=True)
    no = models.PositiveIntegerField(default=0)
    page = models.CharField(max_length=1, choices=PAGE_CHOICES)
    title = title = models.CharField(max_length=100, default="")
    text = models.TextField(max_length=250, unique=True, default="")
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return f"{self.no}{self.page} {self.title}"

    class Meta:
        verbose_name_plural = 'Sections'

# 3
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    no = models.PositiveIntegerField(default=0)
    page = models.CharField(max_length=1, choices=PAGE_CHOICES)
    question = models.TextField(max_length=250, unique=True, default="")
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return f"{self.no}{self.page} {self.question}"

# 4
class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    answer = models.TextField(max_length=250, default="")
    correct = models.BooleanField()
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.answer

# 5 ?
class Mp3File(models.Model):
    id = models.AutoField(primary_key=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='mp3_files')
    url = models.FileField(upload_to='media/mp3_files/')  # Pole dla pliku mp3

    def __str__(self):
        return f"MP3 for {self.board.title}"

    class Meta:
        verbose_name_plural = 'MP3 Files'

# 6
class Player(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, unique=True, default="")
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Players'


class Prize(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, unique=True, default="")
    description = models.TextField(max_length=250, unique=True, default="")
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Prizes'


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, unique=True, default="")
    prizes = models.ManyToManyField(Prize, related_name='events')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Events'
