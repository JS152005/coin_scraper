from celery import shared_task
from.models import ScrapingJob, ScrapingTask
from.coinmarketcap import CoinMarketCap
import logging

logger = logging.getLogger(__name__)

@shared_task
def scrape_coin_data(job_id, coin):
    try:
        job = ScrapingJob.objects.get(pk=job_id)
        scraper = CoinMarketCap()
        data = scraper.get_coin_data(coin)
        ScrapingTask.objects.create(job=job, coin=coin, output=data)
        return data
    except ScrapingJob.DoesNotExist:
        logger.error(f"Scraping job with id {job_id} does not exist")
        return {"error": "Scraping job does not exist"}
    except Exception as e:
        logger.error(f"Error scraping coin data: {e}")
        return {"error": str(e)}