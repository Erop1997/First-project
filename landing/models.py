from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Teacher(models.Model):
    fullname = models.CharField(max_length=255)
    teaching_course = models.CharField(max_length=255)
    description = models.TextField(default='default description')

    def __str__(self):
        return self.fullname
# Имя поля = models.ТипПоля(его атрибуты)


class Lead(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.last_name}, номер телефона - {self.phone_number}. Курс - {self.course}'


# атрибут null = по-умолчанию во всех полях False. Недобходим для определения обязательности внесения информации в какое-либо поле, так как в базе данных все поля по-умолчанию должны быть заполнены.

#ForeignKey - типо поля один-кодному 
# Необходимо для связи какого-либо поля с другой моделью


# Есть три сценария действий базы данных, после удаления какой-либо модели к которой налажена связь (ForeignKey).
# 1 - Если модель была удалена, то будет удален и столбец в таблице, который ссылался на эту модель - models.CASCADE
# 2 - Если модель была удалена, то в полях столбца, который ссылался на эту модель, будет значение null - models.SET_NULL
# 3 - Если модель была удалена, то значения полей, которые ссылались на эту модель, сохраняться - models.PROTECT
