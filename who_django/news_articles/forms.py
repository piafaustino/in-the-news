from django import forms
from .models import NewsArticle

class NewsArticleForm(forms.Form):
	'''
	title = forms.CharField(max_length=300)
	relevance_ranking = forms.FloatField()
	date = forms.DateField()
	source = forms.CharField(max_length=20)
	link = forms.CharField(max_length=300)
	article = forms.CharField(widget=forms.Textarea,required=False)
	author = forms.CharField(max_length=300,required=False)
	location = forms.CharField(max_length=300,required=False)
	accident_count = forms.CharField(max_length=300,required=False)
	byline = forms.CharField(max_length=300,required=False)
	language = forms.CharField(max_length=20,required=False)
	kicker = forms.CharField(max_length=300,required=False)
	'''

	exclude_choices = [
		('Yes','Yes'),
		]
	exclude_label = 'EXCLUDE?'
	exclude = forms.MultipleChoiceField(label=exclude_label, choices=exclude_choices, widget=forms.CheckboxSelectMultiple(),required=False)

	report_type_choices = (
		('-','-'),
		('Straight News','Straight News'),
		('Feature Article', 'Feature Article'),
		('Commentary or Editorial', 'Commentary or Editorial'),
		('In-Depth or Explanatory Report', 'In-Depth or Explanatory Report')
		)

	report_type = forms.ChoiceField(label = "1. What type of report is it?", choices=report_type_choices,required=False)

	dominant_topic_label = "2. What is the dominant topic of the report? (tick all that apply)"
	dominant_topic_choices = (
		('Road Crashes','Road Crashes'),
		('Formulation of legislation/local ordinances','Formulation of legislation/local ordinances'),
		('Enforcement of existing laws/ordinances','Enforcement of existing laws/ordinances'),
		('Road safety as a public health issue','Road safety as a public health issue'),
		('Road infrastructure (repair, maintenance)','Road infrastructure (repair, maintenance)'),
		('Driver education or training','Driver education or training'),
		('Reports on traffic congestion','Reports on traffic congestion'),
		('Traffic advisories','Traffic advisories'),
		('Automobile Industry standards','Automobile Industry standards'),
		('Speed limit enforcement','Speed limit enforcement'),
		('Use of helmets','Use of helmets'),
		('Seatbelt use','Seatbelt use'),
		('Others','Others')
		)
	dominant_topic = forms.MultipleChoiceField(label = dominant_topic_label, choices=dominant_topic_choices, widget=forms.CheckboxSelectMultiple(),required=False)

	road_crash_label = "3. Is this story about a specific road crash incident?"
	road_crash_choices = (
		('-','-'),
		('Yes', 'Yes (Proceed to Step 4)'),
		('No', 'No')
		)
	road_crash = forms.ChoiceField(label=road_crash_label, choices=road_crash_choices)

	road_crash_vehicles_label = "4. If a report about a road crash (a), how many vehicles were involved?"
	road_crash_vehicles = forms.IntegerField(label=road_crash_vehicles_label,required=False)


	vehicle_cat_label = "5. What categories of transportation are mentioned involved in the incident? (tick all that apply)"
	vehicle_cat_choices = (
		('car','car'),
		('van','van'),
		('motorcycle','motorcycle'),
		('bicycle','bicycle'),
		('delivery trucks','delivery trucks'),
		('jeepneys','jeepneys'),
		('tricycles','tricycles'),
		('school service','school service'),
		('armored vehicles','armored vehicles'),
		('ambulance','ambulance'),
		('garbage truck','garbage truck'),
		('tow trucks','tow trucks'),
		(' government vehicles',' government vehicles'),
		('bus','bus')
		)
	vehicle_cat = forms.MultipleChoiceField(label=vehicle_cat_label, choices=vehicle_cat_choices, widget=forms.CheckboxSelectMultiple(),required=False)

	killed = forms.IntegerField(label="6a. How many victims were involved? (killed)",required=False)
	killed_reported = forms.IntegerField(label="6b. How many were victims were identified/reported about in further detail? (killed)",required=False)

	injured = forms.IntegerField(label="7a. How many victims were involved? (injured)",required=False)
	injured_reported = forms.IntegerField(label="7b. How many were victims were identified/reported about in further detail? (injured)",required=False)

	ongoing_coverage_label = "8. Is this article part of ongoing or follow-up coverage of a single incident?"
	ongoing_coverage = forms.CharField(label=ongoing_coverage_label, max_length=100,required=False)

	potential_cause_choices = (
		('Alcohol','Alcohol'),
		('Drugs','Drugs'),
		('Fatigue','Fatigue'),
		('Lack of driver education','Lack of driver education'),
		('Speeding','Speeding'),
		('Mobile Phone use while driving','Mobile Phone use while driving'),
		('Lack of proper road signs','Lack of proper road signs'),
		('Poor road conditions','Poor road conditions'),
		('Poor visibility/lack of lighting','Poor visibility/lack of lighting'),
		('Road obstruction','Road obstruction'),
		('Loss of brakes','Loss of brakes'),
		('Dilapidated vehicle','Dilapidated vehicle'),
		('Entire vehicle combustions','Entire vehicle combustions')
		)

	potential_cause_label = "9. Did the report identify the potential cause(s) of the road crash?"

	potential_cause = forms.MultipleChoiceField(label=potential_cause_label,
		choices=potential_cause_choices,
		widget=forms.CheckboxSelectMultiple(),required=False)

	region_label = "region"
	region = forms.CharField(label=region_label, max_length=100,required=False)

	city_municipality_label = "city/municipality"
	city_municipality = forms.CharField(label=city_municipality_label, max_length=100,required=False)

	specific_location_label = "specific location"
	specific_location = forms.CharField(label=specific_location_label, max_length=100,required=False)

	larger_context_label = "11. Does the report relate the accident to a broader cause or mention a larger context?"
	larger_context_choices = (
		('-','-'),
		('Yes','Yes'),
		('No','No')
		)
	larger_context = forms.ChoiceField(label=larger_context_label,
		choices=larger_context_choices,required=False)

	solutions_choices = (
		('Laws','Laws'),
		('Improvement of Driver Education','Improvement of Driver Education'),
		('Improvement of Pedestrian Education','Improvement of Pedestrian Education'),
		('Change in individual habits','Change in individual habits'),
		('Improvement of infrastructure','Improvement of infrastructure'),
		('Construction of new roads','Construction of new roads'),
		('Improvement of traffic management','Improvement of traffic management'),
		('Improvement of public transport','Improvement of public transport'),
		('Stricter process for getting a drivers license','Stricter process for getting a drivers license'),
		('Stricter process for getting a public transport franchise','Stricter process for getting a public transport franchise'),
		('Stricter process of vehicle registration','Stricter process of vehicle registration'),
		('Improved vehicle maintenance','Improved vehicle maintenance'),
		('Improvement of working conditions in transport sector','Improvement of working conditions in transport sector'),
		('Use of helmet or seat belts','Use of helmet or seat belts'),
		('Implementation of speed limits and other local ordinances','Implementation of speed limits and other local ordinances'),
		('Routine safety inspection','Routine safety inspection'),
		('Automotive industry standards or new tech','Automotive industry standards or new tech'),
		('Others','Others')
		)
	solutions_label = "13. What solutions are discussed? (tick all that apply)"
	solutions = forms.MultipleChoiceField(label=solutions_label,choices=solutions_choices,widget=forms.CheckboxSelectMultiple(),required=False)

	statistics_choices = (
		('-','-'),
		('Yes','Yes'),
		('No','No')
		)
	statistics_label = "14. Are there statistics mentioned in the report?"
	statistics = forms.ChoiceField(label=statistics_label,choices=statistics_choices,required=False)

	stat_scope_label = "15. What scope of statistics on road safety are used?"
	stat_scope_choices = (
		('-','-'),
		('City or municipality wide','City or municipality wide'),
		('Regional','Regional'),
		('National','National'),
		('International','International'),
		('Others','Others')
		)
	stat_scope = forms.ChoiceField(label=stat_scope_label,choices=stat_scope_choices,required=False)

	orgs_choices = (
		('Word Health Organization','Word Health Organization'),
		('Philippine National Police','Philippine National Police'),
		('Metropolitan Manila Development Authority','Metropolitan Manila Development Authority'),
		('Department of Transportation and Communication','Department of Transportation and Communication'),
		('Department of Health','Department of Health'),
		('National Statistical Coordination Board','National Statistical Coordination Board'),
		('Non-government organizations','Non-government organizations'),
		('Academic institutions','Academic institutions'),
		('Others','Others')
		)
	orgs_label = "16. Who are some of the institutions or organizations cited as sources in the report?"
	orgs = forms.MultipleChoiceField(label=orgs_label,choices=orgs_choices,widget=forms.CheckboxSelectMultiple(),required=False)

	resp_group_choices = (
		('Vehicle users','Vehicle users'),
		('Public officials','Public officials'),
		('Government agencies','Government agencies'),
		('Civil society','Civil society'),
		('Transport sector leaders','Transport sector leaders'),
		('Transport sector workers','Transport sector workers'),
		('Others','Others')
		)
	resp_group_label = "17. Does the report mention any agency/group as bearing responsibility for road accidents/improving road safety? (tick all that apply)"
	resp_group = forms.MultipleChoiceField(label=resp_group_label,choices=resp_group_choices,widget=forms.CheckboxSelectMultiple(),required=False)

	tone_choices = (
		('-','-'),
		('Neutral','Neutral'),
		('Optimistic','Optimistic'),
		('Pessimistic','Pessimistic'),
		('Advocating Change','Advocating Change'),
		('Choice','Choice')
		)
	tone_label = "18. What's the tone of the report?"
	tone = forms.ChoiceField(label=tone_label,choices=tone_choices,required=False)

	completed = forms.ChoiceField(label='Survey Finished?',choices=(('-','-'),('Yes','Yes'),('No','No')),required=False)
