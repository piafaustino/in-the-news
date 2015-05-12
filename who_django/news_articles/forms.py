from django import forms
from .models import NewsArticle

class ListFiltersForm(forms.Form):
	pass

class NewsArticleForm(forms.Form):

	rater_choices = [
		('-','-'),
		('mavie','mavie'),
		('candice','candice'),
		('pia','pia'),
		]
	rater_label = 'Rater:'
	rater = forms.ChoiceField(label=rater_label,choices=rater_choices)


	exclude_choices = [
		('-','-'),
		('Yes','Yes'),
		]
	exclude_label = 'EXCLUDE?'
	exclude = forms.ChoiceField(label=exclude_label, choices=exclude_choices,required=False)

	report_type_choices = (
		('-','-'),
		('Straight News','Straight News'),
		('Feature Article', 'Feature Article'),
		('Commentary or Editorial', 'Commentary or Editorial'),
		('In-Depth or Explanatory Report', 'In-Depth or Explanatory Report'),
		('Others','Others')
		)
	report_type = forms.ChoiceField(label = "1. What type of report is it?", choices=report_type_choices,required=False)
	report_type_others = forms.CharField(label="Others", max_length=100, required=False)

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
	dominant_topic_others = forms.CharField(label="Others", max_length=100, required=False)

	road_crash_label = "3. Is this story about a specific road crash incident?"
	road_crash_choices = (
		('-','-'),
		('Yes', 'Yes (Proceed to Step 4)'),
		('No', 'No')
		)
	road_crash = forms.ChoiceField(label=road_crash_label, choices=road_crash_choices)

	road_crash_vehicles_label = "4. If a report about a road crash (a), how many vehicles were involved?"
	road_crash_vehicles = forms.IntegerField(label=road_crash_vehicles_label,required=False)

	vehicle_cat_label = "5a. What categories of transportation are involved in the incident?"
	vehicle_cat_choices = (
		('Private use vehicle','Private use vehicle'),
		('Commercial use','Commercial use'),
		('Government use vehicle','Government use vehicle'),
		('Public utility vehicle','Public utility vehicle'),
		('Others','Others')
		)
	vehicle_cat = forms.MultipleChoiceField(label=vehicle_cat_label, choices=vehicle_cat_choices, widget=forms.CheckboxSelectMultiple(),required=False)
	vehicle_cat_others = forms.CharField(label="Others", max_length=100, required=False)

	vehicle_type_label = ("5b. What type of vehicles are involved in the incident?")
	vehicle_type_choices = (
		('bicycle','bicycle'),
		('motorcycle','motorcycle'),
		('habal-habal','habal-habal'),
		('pedicab','pedicab'),
		('tricycle','tricycle'),
		('kuliglig','kuliglig'),
		('car','car'),
		('van','van'),
		('truck','truck'),
		('jeepney','jeepney'),
		('multi-cab','multi-cab'),
		('school bus','school bus'),
		('armored vehicle','armored vehicle'),
		('ambulance','ambulance'),
		('taxi','taxi'),
		('bus','bus'),
		('Asian Utility Vehicle (FX)','Asian Utility Vehicle (FX)'),
		('Others','Others')
		)
	vehicle_type = forms.MultipleChoiceField(label=vehicle_type_label, choices=vehicle_type_choices, widget=forms.CheckboxSelectMultiple(),required=False)
	vehicle_type_others = forms.CharField(label="Others", max_length=100, required=False)

	killed = forms.IntegerField(label="6a. How many victims were killed in the car crash? (killed)",required=False)
	killed_reported = forms.CharField(label="6b. How many of the fatalities were described in further detail and how?", widget=forms.Textarea, required=False)

	injured = forms.IntegerField(label="How many victims were injured in the car crash?",required=False)
	injured_reported = forms.CharField(label="7b. How many of the injured were described in further detail and how?", widget=forms.Textarea, required=False)

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
		('Entire vehicle combustions','Entire vehicle combustions'),
		('Others','Others')
		)

	potential_cause_label = "9. Did the report identify the potential cause(s) of the road crash?"


	potential_cause = forms.MultipleChoiceField(label=potential_cause_label,
		choices=potential_cause_choices,
		widget=forms.CheckboxSelectMultiple(),required=False)
	potential_cause_others = forms.CharField(label="Others", max_length=100, required=False)

	#the question on item 11 is on the html template.

	region_label = "province"
	region = forms.CharField(label=region_label, max_length=100,required=False)

	city_municipality_label = "city/municipality"
	city_municipality = forms.CharField(label=city_municipality_label, max_length=100,required=False)

	specific_location_label = "specific location"
	specific_location = forms.CharField(label=specific_location_label, max_length=100,required=False)

	accident_time_of_day_label = "11. What time of day did the accident take place?"
	accident_time_of_day = forms.CharField(label=accident_time_of_day_label, max_length=100,required=False)

	larger_context_label = "12. Does the report relate the accident to a broader cause or mention a larger context?"
	larger_context_choices = (
		('-','-'),
		('Yes','Yes'),
		('No','No')
		)
	larger_context = forms.ChoiceField(label=larger_context_label,
		choices=larger_context_choices,required=False)

	solutions_choices = (
		('Enforcment of speed limits', 'Enforcement of speed limits'),
		('Reduction of speed limits', 'Reduction of speed limits'),
		('Improvement of traffic enforcement', 'Improvement of traffic enforcement'),
		('Stricter drivers license regulation', 'Stricter drivers license regulation'),
		('Stricter public transport franchise regulation','Stricter public transport franchise regulation'),
		('Improvement of working conditions in transport sector','Improvement of working conditions in transport sector'),
		('Implementation of safety inspections on public transport','Implementation of safety inspections on public transport'),
		('Improvement of road infrastructure','Improvement of road infrastructure'),
		('Improvement of infrastructure for pedestrians','Improvement of infrastructure for pedestrians'),
		('Improvement of infrastructure for cyclists','Improvement of infrastructure for cyclists'),
		('Improvement of mass public transport infrastructure','Improvement of mass public transport infrastructure'),
		('Installation of road signs','Installation of road signs'),
		('Improved visibility or accuracy of road signs','Improved visibility or accuracy of road signs'),
		('Stricter automotive industry standards','Stricter automotive industry standards'),
		('Safer vehicle technology','Safer vehicle technology'),
		('Improved vehicle maintenance','Improved vehicle maintenance'),
		('Road user education','Road user education'),
		('Use of helmets','Use of helmets'),
		('Use of seat belts','Use of seat belts'),
		('Avoiding mobile use while driving','Avoiding mobile use while driving'),
		('Use of child restraints','Use of child restraints'),
		('Improvement of post-crash emergency response','Improvement of post-crash emergency response'),
		('Others','Others')
		)

	solutions_label = "13. What solutions are discussed? (tick all that apply)"
	solutions = forms.MultipleChoiceField(label=solutions_label,choices=solutions_choices,widget=forms.CheckboxSelectMultiple(),required=False)
	solutions_others = forms.CharField(label="Others", max_length=100, required=False)

	statistics_choices = (
		('-','-'),
		('Yes','Yes'),
		('No','No')
		)
	statistics_label = "14. Are there statistics mentioned in the report?"
	statistics = forms.ChoiceField(label=statistics_label,choices=statistics_choices,required=False)

	stat_scope_label = "15. What scope of statistics on road safety are used?"
	stat_scope_choices = (
		('City or municipality wide','City or municipality wide'),
		('Regional','Regional'),
		('National','National'),
		('International','International'),
		('Others','Others')
		)
	stat_scope = forms.MultipleChoiceField(label=stat_scope_label,choices=stat_scope_choices,widget=forms.CheckboxSelectMultiple(),required=False)
	stat_scope_others = forms.CharField(label="Others", max_length=100, required=False)

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
	orgs_others = forms.CharField(label="Others", max_length=100, required=False)

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
	resp_group_others = forms.CharField(label="Others", max_length=100, required=False)

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

