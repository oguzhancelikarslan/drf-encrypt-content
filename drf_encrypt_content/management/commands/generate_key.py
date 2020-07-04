from cryptography.fernet import Fernet
from django.core.management import BaseCommand


class Command(BaseCommand):
    """
        We have to keep this key in a safe place.
        if we lose it, we cannot decrypt data encrypted with this key.
    """

    help = 'Creates new key to encrypt data.'

    def handle(self, *args, **options):
        key = Fernet.generate_key()
        self.stdout.write(self.style.WARNING(
            'Keep this key in a safe place. if you lose the key, '
            'you will no longer be able to decrypt data that was encrypted with this key.')
        )
        self.stdout.write('Key: %s' % key.decode("utf-8"))
        self.stdout.write(self.style.SUCCESS('Successfully generated'))
