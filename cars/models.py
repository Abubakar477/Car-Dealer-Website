from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.core.validators import RegexValidator

class Car(models.Model):
    province_choice = (
        ('Sindh', 'Sindh'),
        ('Punjab', 'Punjab'),
        ('Khyber Pakhtunkhwa', 'Khyber Pakhtunkhwa'),
        ('Balochistan', 'Balochistan'),
        ('Islamabad Capital Territory', 'Islamabad Capital Territory'),
    )

    city_choice = (
        ('KHI', 'Karachi'),
        ('LHR', 'Lahore'),
        ('ISB', 'Islamabad'),
        ('RWP', 'Rawalpindi'),
        ('PEW', 'Peshawar'),
        ('QTA', 'Quetta'),
        ('MUX', 'Multan'),
        ('HYD', 'Hyderabad'),
        ('FSD', 'Faisalabad'),
        ('GJR', 'Gujranwala'),
    )

    year_choice = [(r, r) for r in range(2000, datetime.now().year + 1)]

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255, default='Car Title')
    city = models.CharField(choices=city_choice, max_length=100, default='KHI')
    province = models.CharField(choices=province_choice, max_length=100, default='Sindh')
    color = models.CharField(max_length=100, default='White')
    model = models.CharField(max_length=100, default='2020')
    year = models.IntegerField(('year'), choices=year_choice, default=datetime.now().year)
    condition = models.CharField(max_length=100, default='New')
    price = models.IntegerField(default=1000000)
    description = RichTextField(default='Description of the car')
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices, default='Cruise Control')
    body_style = models.CharField(max_length=100, default='Sedan')
    engine = models.CharField(max_length=100, default='1.8L')
    transmission = models.CharField(max_length=100, default='Automatic')
    interior = models.CharField(max_length=100, default='Black')
    miles = models.IntegerField(default=0)
    doors = models.CharField(choices=door_choices, max_length=10, default='4')
    passengers = models.IntegerField(default=4)
    vin_no = models.CharField(max_length=100, default='UNKNOWN')
    milage = models.IntegerField(default=0)
    fuel_type = models.CharField(max_length=50, default='Petrol')
    no_of_owners = models.CharField(max_length=100, default='First Owner')
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    # ✅ Only YouTube video ID stored here
    youtube_id = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[RegexValidator(regex=r'^[\w-]{11}$', message="Enter a valid 11-character YouTube video ID.")]
    )

    def __str__(self):
        return self.car_title
