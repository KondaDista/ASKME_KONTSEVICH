from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


class QuestionManager(models.Manager):
    def get_all_questions(self):
        return self.all().annotate(num_answers=Count('answer')).annotate(likes_count=Count('likequestion'))

    def get_question(self, question_id):
        return self.filter(id__exact=question_id).first()

    def get_questions_by_tag(self, tag_name):
        return self.filter(tags__name__exact=tag_name)

    def get_new_questions(self):
        return self.filter(status__contains='new')

    def get_hot_questions(self):
        return QuestionManager.get_all_questions(self).order_by('-likes_count')

    def get_tags(self):
        return TagQuestion.objects

    def get_likes(self):
        return LikeQuestion.objects


class AnswerManager(models.Manager):
    def get_answer_by_question(self, question_id):
        return self.filter(question__id__exact=question_id)


class LikeManager(models.Manager):
    def get_likes(self):
        return LikeQuestion.objects


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
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags = models.ManyToManyField(TagQuestion)

    objects = QuestionManager()

    def __str__(self):
        return str(self.title)


class Answer(models.Model):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answered = models.BooleanField()

    objects = AnswerManager()

    def __str__(self):
        return str(self.question) + " => AnswerID = " + str(self.id)


class LikeQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    objects = LikeManager()

    class Meta:
        unique_together = ('question', 'user')

    def __str__(self):
        return str(self.question) + " => UserID = " + str(self.user)


class LikeAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    objects = LikeManager()

    class Meta:
        unique_together = ('answer', 'user')

    def __str__(self):
        return str(self.answer) + " => UserID = " + str(self.user)


class DislikeQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    objects = LikeManager()

    class Meta:
        unique_together = ('question', 'user')

    def __str__(self):
        return str(self.question) + " => UserID = " + str(self.user)


class DislikeAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    objects = LikeManager()

    class Meta:
        unique_together = ('answer', 'user')

    def __str__(self):
        return str(self.answer) + " => UserID = " + str(self.user)
