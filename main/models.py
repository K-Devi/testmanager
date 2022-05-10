from django.db import models



class Teachers(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.full_name


class Course(models.Model):
    title = models.CharField('Name', max_length=255)
    course_slug = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField('Name', max_length=255)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField('Name', max_length=255)

    section = models.ForeignKey(Section, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class QuestionType(models.Model):
    type = models.CharField('Type', max_length=10)

    def __str__(self):
        return self.type


class Question(models.Model):
    question = models.TextField(max_length=300)
    type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_slug = models.CharField(max_length=200)


    def __str__(self):
        return self.question
