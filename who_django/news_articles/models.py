from django.db import models
from django.utils import timezone

class NewsArticle(models.Model):
	#news article fields
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
	order_id = models.IntegerField(blank=True, null=True)
	accident_time_of_day = models.CharField(max_length=300,blank=True,null=True)

	#video article fields
	view_count = models.IntegerField(blank=True, null=True)
#	order_id = models.IntegerField(blank=True, null=True)
#	relevance_ranking = models.FloatField()
#	language = models.CharField(max_length=20, blank=True,null=True)
#	title = models.CharField(max_length=300,null=True, blank=True) -
#	accident_count = models.CharField(max_length=300, blank=True,null=True)
#	date = models.DateField(null=True, blank=True)
	like_count = models.IntegerField(blank=True, null=True)
	comment_count = models.IntegerField(blank=True, null=True)
#	source = models.CharField(max_length=20,null=True)
	duration = models.CharField(max_length=20,null=True)
	favorite_count = models.IntegerField(blank=True, null=True)
	youtube_id = models.CharField(max_length=20,null=True)
	dislike_count = models.IntegerField(blank=True, null=True)
	link = models.CharField(max_length=300,null=True)
#	order_id = models.IntegerField(blank=True, null=True)
#	accident_time_of_day = models.CharField(max_length=300,blank=True,null=True)


	#type of news (video or article)
	news_type = models.CharField(max_length=300, blank=True, null=True)

	#rater
	rater = models.CharField(max_length=300, blank=True, null=True)

	#survey questions:
	report_type = models.CharField(max_length=1000,blank=True,null=True)
	dominant_topic = models.CharField(max_length=1000,blank=True,null=True)
	road_crash = models.CharField(max_length=1000,blank=True,null=True)
	road_crash_vehicles = models.CharField(max_length=1000,blank=True,null=True)
	vehicle_cat = models.CharField(max_length=1000,blank=True,null=True)
	killed = models.IntegerField(blank=True,null=True)
	killed_reported = models.CharField(max_length=1000,blank=True,null=True)
	injured = models.IntegerField(blank=True,null=True)
	injured_reported = models.CharField(max_length=1000,blank=True,null=True)
	ongoing_coverage = models.CharField(max_length=1000,blank=True,null=True)
	potential_cause = models.CharField(max_length=1000,blank=True,null=True)
	larger_context = models.CharField(max_length=1000,blank=True,null=True)
	solutions = models.CharField(max_length=1000,blank=True,null=True)
	statistics = models.CharField(max_length=1000,blank=True,null=True)
	stat_scope = models.CharField(max_length=1000,blank=True,null=True)
	orgs = models.CharField(max_length=1000,blank=True,null=True)
	resp_group = models.CharField(max_length=1000,blank=True,null=True)
	tone = models.CharField(max_length=1000,blank=True,null=True)
	completed = models.CharField(max_length=1000,blank=True,null=True)
	vehicle_type = models.CharField(max_length=1000,blank=True,null=True)

	region = models.CharField(max_length=1000, blank=True,null=True)
	city_municipality = models.CharField(max_length=1000, blank=True,null=True)
	specific_location = models.CharField(max_length=1000, blank=True,null=True)

	exclude = models.CharField(max_length=1000, blank=True, null=True)

	report_type_others = models.CharField(max_length=1000, blank=True, null=True)
	dominant_topic_others = models.CharField(max_length=1000, blank=True, null=True)
	vehicle_cat_others = models.CharField(max_length=1000, blank=True, null=True)
	potential_cause_others = models.CharField(max_length=1000, blank=True, null=True)
	solutions_others = models.CharField(max_length=1000, blank=True, null=True)
	stat_scope_others = models.CharField(max_length=1000, blank=True, null=True)
	orgs_others = models.CharField(max_length=1000, blank=True, null=True)
	resp_group_others = models.CharField(max_length=1000, blank=True, null=True)
	vehicle_type_others = models.CharField(max_length=1000, blank=True, null=True)

	def __str__(self):
		return self.title
# Create your models here
