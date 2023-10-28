import logging
from typing import Final

from django.core.management.base import BaseCommand
from django.db import IntegrityError

from api.models import Contact


class Command(BaseCommand):
    help = "Generate contacts and contact data"
    MINIMAL_AMOUNT_OF_CONTACTS: Final[int] = 1

    def handle(self, *args, **options) -> None:
        logger = logging.getLogger("django")
        current_amount_of_contacts = Contact.objects.count()

        amount_needed = self.MINIMAL_AMOUNT_OF_CONTACTS - current_amount_of_contacts

        if amount_needed > 0:
            logger.info(f"Current amount of contacts: {current_amount_of_contacts} and {amount_needed} needed")

            for _ in range(amount_needed):
                try:
                    contact = Contact.objects.create(name="Somebody", phone_number="+380688523899")
                    contact.save()
                except IntegrityError:
                    logger.info("A one newly created contact is not unique and has been skipped")

            logger.info(f"Newly created contact amount: {amount_needed}")

        else:
            logger.info("Current amount of contacts is enough. No new contact created.")

        # newly_created_contact_data = 0
        # for contact in Contact.objects.all():
        #     has_contact_data = Contact.objects.filter(contactdata__contact_id=contact.id).exists()
        #     if not has_contact_data:
        #         management.call_command("generate_contact_data", id=contact.id)
        #         newly_created_contact_data += 1
        #
        # logger.info(f"Newly created contact data amount: {newly_created_contact_data}")
