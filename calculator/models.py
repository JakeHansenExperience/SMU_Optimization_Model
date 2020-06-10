from django.db import models

# Create your models here.

class Plant(models.Model):
    plant_name = models.CharField(max_length=255)
    def __str__(self):
        return self.plant_name

    selected = models.BooleanField(default=False)
    # configuration = models.ForeignKey(Configuration, on_delete=models.CASCADE)

# class PlantTemp(models.Model):
#     plant_name = models.CharField(max_length=255)
#     configuration = models.ForeignKey(Configuration, on_delete=models.CASCADE)


class Configuration(models.Model):
    configuration_name = models.CharField(max_length=255)
    def __str__(self):
        return self.configuration_name




class Demand(models.Model):
    demand_name = models.CharField(max_length=255)
    def __str__(self):
        return self.demand_name

    interior_heavy_demand = models.DecimalField(max_digits=10, decimal_places=2)
    insulated_glass_demand = models.DecimalField(max_digits=10, decimal_places=2)
    laminated_simple_demand = models.DecimalField(max_digits=10, decimal_places=2)
    laminated_complex_demand = models.DecimalField(max_digits=10, decimal_places=2)
    specialty_demand = models.DecimalField(max_digits=10, decimal_places=2)

class Function(models.Model):
    function_name = models.CharField(max_length=255)
    def __str__(self):
        return self.function_name

    function_id = models.IntegerField()

class Layout(models.Model):
    layout_name = models.CharField(max_length=255)
    def __str__(self):
        return self.layout_name



class PlantResult(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    result = models.ForeignKey(Layout, on_delete=models.CASCADE)


    interior_heavy_result = models.DecimalField(max_digits=10,decimal_places = 2)
    insulated_glass_result = models.DecimalField(max_digits=10,decimal_places = 2)
    laminated_complex_result = models.DecimalField(max_digits=10,decimal_places = 2)
    laminated_simple_result =  models.DecimalField(max_digits=10,decimal_places = 2)
    specialty_result = models.DecimalField(max_digits=10,decimal_places = 2)




class Station(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    workers = models.DecimalField(max_digits= 6, decimal_places = 2)
    shifts = models.IntegerField(default=0)
    wages = models.DecimalField(max_digits= 6, decimal_places = 2)
    labor_dollar_hr = models.DecimalField(max_digits=6, decimal_places=2)
    energy_dollar_hr = models.DecimalField(max_digits=6, decimal_places=2)
    variable_dollar_hr = models.DecimalField(max_digits=6, decimal_places=2)
    interior_heavy_capacity = models.DecimalField(max_digits=10,decimal_places = 2)
    insulated_glass_capacity = models.DecimalField(max_digits=10,decimal_places = 2)
    laminated_complex_capacity = models.DecimalField(max_digits=10,decimal_places = 2)
    laminated_simple_capacity =  models.DecimalField(max_digits=10,decimal_places = 2)
    specialty_capacity = models.DecimalField(max_digits=10,decimal_places = 2)
    time_hr_month = models.DecimalField(max_digits=10,decimal_places = 2)
    time_hr_shift = models.DecimalField(max_digits=10,decimal_places = 2)
    days = models.IntegerField(default=0)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)



# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text
