from django.db import models
from django.utils import timezone

class NewsArticle(models.Model):
	title = models.CharField(max_length=300,null=True, blank=True)
	relevance_ranking = models.FloatField()
	date = models.DateField(null=True, blank=True)
	source = models.CharField(max_length=20,null=True)
	link = models.CharField(max_length=300,null=True)
	article = models.TextField(blank=True,null=True)
	author = models.CharField(max_length=300, blank=True,null=True)
	location = models.CharField(max_length=300, blank=True,null=True)
	accident_count = models.CharField(max_length=300, blank=True,null=True)
	byline = models.CharField(max_length=300, blank=True,null=True)
	language = models.CharField(max_length=20, blank=True,null=True)
	kicker = models.CharField(max_length=300,blank=True,null=True)

	dominant_topic = models.CharField(max_length=300,blank=True,null=True)
	road_crash = models.CharField(max_length=300,blank=True,null=True)
	vehicle_cat = models.CharField(max_length=300,blank=True,null=True)
	killed = models.IntegerField(blank=True,null=True)
	killed_reported = models.IntegerField(blank=True,null=True)
	injured = models.IntegerField(blank=True,null=True)
	injured_reported = models.IntegerField(blank=True,null=True)
	ongoing_coverage = models.CharField(max_length=300,blank=True,null=True)
	potential_cause = models.CharField(max_length=300,blank=True,null=True)
	larger_context = models.CharField(max_length=300,blank=True,null=True)
	solutions = models.CharField(max_length=300,blank=True,null=True)
	statistics = models.CharField(max_length=300,blank=True,null=True)
	stat_scope = models.CharField(max_length=300,blank=True,null=True)
	orgs = models.CharField(max_length=300,blank=True,null=True)
	resp_group = models.CharField(max_length=300,blank=True,null=True)
	tone = models.CharField(max_length=300,blank=True,null=True)

	def __str__(self):
		return self.title
# Create your models here
