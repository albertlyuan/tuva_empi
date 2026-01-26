from django.core.management.base import BaseCommand

from main.services.matching.matching_service import MatchingService
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Starts MatchingService"
    logger.info("matching service")

    def handle(self, *args: str, **options: str) -> None:
        MatchingService().start()
