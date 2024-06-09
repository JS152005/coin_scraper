from django.test import TestCase
from .models import ScrapingJob, ScrapingTask
from .views import start_scraping, scraping_status

class ScrapingJobTestCase(TestCase):
    def setUp(self):
        self.job = ScrapingJob.objects.create()

    def test_job_creation(self):
        self.assertIsInstance(self.job, ScrapingJob)
        self.assertEqual(self.job.status, ScrapingJob.PENDING)

    def test_job_status_update(self):
        self.job.status = ScrapingJob.IN_PROGRESS
        self.job.save()
        self.assertEqual(self.job.status, ScrapingJob.IN_PROGRESS)

class ScrapingTaskTestCase(TestCase):
    def setUp(self):
        self.task = ScrapingTask.objects.create(coin='Bitcoin')

    def test_task_creation(self):
        self.assertIsInstance(self.task, ScrapingTask)
        self.assertEqual(self.task.coin, 'Bitcoin')

class ViewTestCase(TestCase):
    def test_start_scraping_view(self):
        response = self.client.post('/api/taskmanager/start_scraping', data=['Bitcoin', 'Ethereum'])
        self.assertEqual(response.status_code, 201)
        self.assertIn('job_id', response.data)

    def test_scraping_status_view(self):
        job = ScrapingJob.objects.create()
        response = self.client.get(f'/api/taskmanager/scraping_status/{job.job_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.data)