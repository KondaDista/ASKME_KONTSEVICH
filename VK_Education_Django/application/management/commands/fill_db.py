from django.core.management import BaseCommand

QUESTIONS = [
    {
        'title': f'Help Title-{i}',
        'id': i,
        'text': f'Some text for question number-{i}'
    }
    for i in range(1, 25)
]

ANSWERS = [
    {
        'id': i,
        'text': f'Some quick example text to build on the card title and make up the bulk of the cards content. Some quick example text to build on the card title and make up the bulk of the cards content. Number-{i}'
    }
    for i in range(1, 42)
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("HI")