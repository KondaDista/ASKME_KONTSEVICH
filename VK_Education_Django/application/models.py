from django.contrib.auth.models import User
from django.db import models


class QuestionManager(models.Manager):
    def get_new_question(self):
        return self.filter(status__contains='new')

    def get_hot_question(self):
        return self.filter(status__contains='hot')

    def get_tags(self):
        return TagQuestion.objects.filter(status__contains='hot')


class AnswerManager(models.Manager):
    def get_answer_by_question(self, question_id):
        return self.filter(id_question__id__exact = question_id)


class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login = models.CharField(max_length=255)
    nickname = models.CharField(null=False, max_length=255)
    email = models.CharField(max_length=255)
    avatar = models.ImageField(null=True, blank=True, upload_to='uploads')

    def __str__(self):
        return str(self.login)


class TagQuestion(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Question(models.Model):
    STATUS_CHOICES = [
        ('new', 'New Question'),
        ('hot', 'Hot Question'),
    ]
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    id_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags = models.ManyToManyField(TagQuestion)

    objects = QuestionManager()

    def __str__(self):
        return str(self.title)


class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=255)
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_answered = models.BooleanField()

    objects = AnswerManager()

    def __str__(self):
        return str(self.id_question) + " => AnswerID = " + str(self.id)


class LikeQuestion(models.Model):
    id = models.IntegerField(primary_key=True)
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    id_user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('id_question', 'id_user')

    def __str__(self):
        return str(self.id_question) + " => UserID = " + str(self.id_user)


class LikeAnswer(models.Model):
    id = models.IntegerField(primary_key=True)
    id_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    id_user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('id_answer', 'id_user')

    def __str__(self):
        return str(self.id_answer) + " => UserID = " + str(self.id_user)

# class QuestionTag(models.Model):
#     id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     id_tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#
#
# class QuestionLike(models.Model):
#     id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     id_like = models.ForeignKey(Like, on_delete=models.CASCADE)
#
#
# class AnswerLike(models.Model):
#     id_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
#     id_like = models.ForeignKey(Like, on_delete=models.CASCADE)
