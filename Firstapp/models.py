# from django.db import models


# class Employee(models.Model):
#     eid=models.CharField(max_length=50,unique=True)

#     name = models.CharField(max_length=100)

#     email = models.EmailField()

#     department = models.CharField(max_length=50)

#     salary = models.IntegerField()

# class DeletedEmployee(models.Model):

#     eid = models.CharField(max_length=50)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     salary = models.IntegerField()
#     department = models.CharField(max_length=100)
#     deleted_at = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.name
# from django.db import models
# from django.core.validators import RegexValidator


# gmail_validator = RegexValidator(
#     regex=r'^[a-zA-Z0-9._%+-]+@gmail\.com$',
#     message="Only Gmail addresses are allowed."
# )


# class Employee(models.Model):

#     eid = models.CharField(
#         max_length=50,
#         unique=True
#     )

#     name = models.CharField(
#         max_length=100
#     )

#     email = models.EmailField(
#         validators=[gmail_validator]
#     )

#     department = models.CharField(
#         max_length=50
#     )

#     salary = models.IntegerField()


#     def __str__(self):
#         return self.name
    
# from django.db import models
# from django.core.validators import RegexValidator


# alphabet_validator = RegexValidator(
#     regex=r'^[A-Za-z ]+$',
#     message="Name should contain only alphabets."
# )


# class Employee(models.Model):

#     eid = models.CharField(
#         max_length=50,
#         unique=True
#     )

#     name = models.CharField(
#         max_length=100,
#         validators=[alphabet_validator]
#     )

#     email = models.EmailField()

#     department = models.CharField(
#         max_length=50,
#         validators=[alphabet_validator]
#     )

#     salary = models.IntegerField()


#     def save(self, *args, **kwargs):

#         # Convert name to capital letters
#         self.name = self.name.upper()

#         # Convert department to capital letters
#         self.department = self.department.upper()

#         super().save(*args, **kwargs)
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


# Only alphabets for name and department
alphabet_validator = RegexValidator(
    regex=r'^[A-Za-z ]+$',
    message="Only alphabets are allowed."
)


# Only gmail.com emails
gmail_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9._%+-]+@gmail\.com$',
    message="Email must end with @gmail.com"
)


class Employee(models.Model):

    eid = models.CharField(
        max_length=50,
        unique=True
    )

    name = models.CharField(
        max_length=100,
        validators=[alphabet_validator]
    )

    email = models.EmailField(
        validators=[gmail_validator]
    )

    department = models.CharField(
        max_length=50,
        validators=[alphabet_validator]
    )

    salary = models.IntegerField(
        validators=[
            MinValueValidator(150000),
            MaxValueValidator(300000)
        ]
    )


    def save(self, *args, **kwargs):

        # Convert to capital letters
        self.name = self.name.upper()
        self.department = self.department.upper()

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
class DeletedEmployee(models.Model):

    eid = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.IntegerField()
    department = models.CharField(max_length=100)
    deleted_at = models.DateTimeField(auto_now_add=True)

from django.core.validators import MinValueValidator,MaxValueValidator

salary = models.IntegerField(
    validators=[
        MinValueValidator(150000), MaxValueValidator(300000)
    ]
)


from django.core.validators import RegexValidator


alphabet_validator = RegexValidator(
    regex=r'^[A-Za-z ]+$',
    message="Department should contain only alphabets."
)


class Employee(models.Model):

    eid = models.CharField(
        max_length=50,
        unique=True
    )

    name = models.CharField(
        max_length=100,
        validators=[alphabet_validator]
    )

    email = models.EmailField()

    department = models.CharField(
        max_length=50,
        validators=[alphabet_validator]
    )

    salary = models.IntegerField()


    def save(self, *args, **kwargs):

        self.name = self.name.upper()
        self.department = self.department.upper()

        super().save(*args, **kwargs)