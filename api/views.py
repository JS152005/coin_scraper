from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import ScrapingJob
from.serializers import ScrapingJobSerializer
from.tasks import scrape_coin_data
from django.http import Http404

@api_view(['POST'])
def start_scraping(request):
    if not isinstance(request.data, list) or not all(isinstance(item, str) for item in request.data):
        return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)
    
    job = ScrapingJob.objects.create(status=ScrapingJob.PENDING)  # Set initial status to PENDING
    for coin in request.data:
        scrape_coin_data.delay(job.job_id, coin)
    return Response({"job_id": job.job_id}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def scraping_status(request, job_id):
    try:
        job = ScrapingJob.objects.get(pk=job_id)
    except ScrapingJob.DoesNotExist:
        raise Http404("Job not found")
    
    serializer = ScrapingJobSerializer(job)
    return Response(serializer.data, status=status.HTTP_200_OK)