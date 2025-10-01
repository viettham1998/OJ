from django.core.management.base import BaseCommand, CommandError
from judge.models import Profile, Organization

class Command(BaseCommand):
    help = "Add an existing user to an organization"

    def add_arguments(self, parser):
        parser.add_argument("username", type=str, help="Username of the user")
        parser.add_argument("org_key", type=str, help="Key (short name) of the organization")

    def handle(self, *args, **options):
        username = options["username"]
        org_key = options["org_key"]

        try:
            user_profile = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise CommandError(f"User with username '{username}' does not exist.")

        try:
            org = Organization.objects.get(short_name=org_key)
        except Organization.DoesNotExist:
            raise CommandError(f"Organization with key '{org_key}' does not exist.")

        user_profile.organizations.add(org)
        user_profile.save()

        self.stdout.write(self.style.SUCCESS(
            f"User '{username}' has been added to organization '{org.name}' ({org.short_name})."
        ))
