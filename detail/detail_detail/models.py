from django.db import models

# Create your models here.

class Owner(models.Model):
    ownername = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

class Car(models.Model):
    title = models.CharField(max_length=200 )
    car_license = models.DateTimeField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField()
    mileage = models.CharField(max_length=100)
    market = models.FloatField()
    Register_time = models.DateTimeField(max_length=100)
    address = models.CharField(max_length=150)
    emission_standard = models.CharField(max_length=100)
    speed_changing_box = models.CharField(max_length=100)
    custom_id = models.CharField(max_length=100)
    discharge = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    address_of_a_car = models.CharField(max_length=100)
    annual_inspection = models.DateTimeField(max_length=50)
    insurance = models.DateTimeField(max_length=50)
    commercial_insuranc = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

class Basic_parameter(models.Model):
    manufacturter = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    seep_changing_box = models.CharField(max_length=30)
    car_body = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    wheel_base = models.CharField(max_length=30)
    trunk = models.CharField(max_length=30)
    weight = models.CharField(max_length=50)
    car = models.ForeignKey(Car , on_delete=models.CASCADE)

class Engine_parameter(models.Model):
    engine = models.CharField(max_length=100)
    discharge = models.FloatField()
    intake_type = models.CharField(max_length=100)
    air_cyinder = models.CharField(max_length=50)
    max_horsepower = models.CharField(max_length=50)
    torque = models.CharField(max_length=50)
    fuel = models.CharField(max_length=50)
    Alimentation = models.CharField(max_length=50)
    emission_standard = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

class Chassis_braking(models.Model):
    drive_mode = models.CharField(max_length=50)
    Power_type = models.CharField(max_length=50)
    Front_suspension_type = models.CharField(max_length=50)
    Rear_suspeusion_type = models.CharField(max_length=50)
    front_brake_type = models.CharField(max_length=50)
    rear_brake_type = models.CharField(max_length=50)
    parking_brake_type = models.CharField(max_length=50)
    front_tire_type = models.CharField(max_length=50)
    rear_tire_type =  models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
# # class Security_configuration(models.Model):
#     pass
# class Exterior_specification(models.Model):
#     pass
# class Interior_collocation(models.Model):
#     pass