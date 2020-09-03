from django.db import models

# Create your models here.
class Build(models.Model):
    """Здание"""
    id = models.AutoField(primary_key=True)
    name=models.CharField('Название',max_length=100)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.id
    class Meta:
        verbose_name="Здание"
        verbose_name_plural="Здания"

class Floor(models.Model):
    """"Этаж"""
    id= models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=100)
    build_id=models.ForeignKey(Build, on_delete=models.CASCADE,db_column='build_id')

    def __str__(self):
        return self.name

    def __int__(self):
        return self.id
    class Meta:
        verbose_name="Этаж"
        verbose_name_plural="Этажи"
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=100)
    floor_id=models.ForeignKey(Floor, on_delete=models.CASCADE,db_column='floor_id')

    def __str__(self):
        return self.name

    def __int__(self):
        return self.id
    class Meta:
        verbose_name="Помещение"
        verbose_name_plural="Помещения"
class People(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField('Имя', max_length=100)
    second_name = models.CharField('Отчество', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    room_id=models.ForeignKey(Room, on_delete=models.CASCADE,db_column='room_id')
    def __str__(self):
        return self.name
    def __int__(self):
        return self.id
    class Meta:
        verbose_name="Арендадержатель"
        verbose_name_plural="Арендадержатели"
