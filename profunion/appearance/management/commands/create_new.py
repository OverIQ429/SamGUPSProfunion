from django.core.management import BaseCommand

from appearance.models import News

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the news')
        parser.add_argument('article', type=str, help='Article of the news')

    def handle(self, *args, **options):
        name = options['name']
        article = options['description']

        self.stdout.write(f"Create new post with name '{name}' and article '{article}'")

        new, created = News.objects.get_or_create(name=name, article=article)
        if created:
            self.stdout.write(f"Created new post {new.name}")
        else:
            self.stdout.write(f"Post with name '{name}' already exists")

        self.stdout.write(self.style.SUCCESS("Products created"))