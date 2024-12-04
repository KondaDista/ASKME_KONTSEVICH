from random import choice, choices, randint
from string import ascii_letters

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string

from application.models import Question, Answer, Profile, TagQuestion, LikeQuestion, LikeAnswer


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, default=5)

    def handle(self, *args, **options):
        ratio = options['ratio']

        bulk_users = [
            User(username='user-' + get_random_string(randint(5, 30), ascii_letters),
                 email='user@mail.com',
                 password='3232')
            for _ in range(ratio)
        ]
        User.objects.bulk_create(bulk_users)

        bulk_profiles = [
            Profile(id = item.id,
                    user=item,
                    login=item.username,
                    nickname=item.username,
                    email=item.email)
            for item in bulk_users
        ]
        Profile.objects.bulk_create(bulk_profiles)
        profiles = Profile.objects.all()

        bulk_tags = [
            TagQuestion(name=get_random_string(randint(3, 10), ascii_letters))
            for _ in range(ratio)
        ]
        TagQuestion.objects.bulk_create(bulk_tags)
        tags = TagQuestion.objects.all()

        bulk_questions = [
            Question(id = item,
                     title=get_random_string(randint(5, 25), ascii_letters),
                     description=get_random_string(randint(50, 200), ascii_letters),
                     user= choice(profiles))
            for item in range(ratio * 10)
        ]
        Question.objects.bulk_create(bulk_questions)
        questions = Question.objects.all()

        for question in questions:
            question.tags.set(choices(tags, k=randint(1, 8)))
            bulk_answer = [
                Answer(text=get_random_string(randint(50, 150), ascii_letters),
                       question=question)
                for _ in range(randint(7, 18))
            ]
            Answer.objects.bulk_create(bulk_answer)
        answers = Answer.objects.all()

        for _ in range(ratio * 100):
            question = choice(questions)
            user = choice(profiles)
            LikeQuestion.objects.get_or_create(question=question, user=user)

        for _ in range(ratio * 100):
            answer = choice(answers)
            user = choice(profiles)
            LikeAnswer.objects.get_or_create(answer=answer, user=user)
