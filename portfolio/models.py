from django.db import models

class Skill(models.Model):
    """Model for current skills.

    Args:
        models (django.model): .
    """
    skill = models.CharField(max_length=50, blank=False,primary_key=True)
    skill_level = models.DecimalField(decimal_places=2, blank=False, max_digits=5)
    work_experience = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self) -> str:
        return f"{self.skill}, Self attested Experience: {self.skill_level*100}%, Years of experience: {self.work_experience} years"

class WorkExperience(models.Model):
    """Model for work experience in profile.

    Args:
        models (django.model): .
    """
    role = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    work_description = models.CharField(max_length=500)
    logo_url = models.URLField()
    is_current_job = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Role: {self.role} in {self.company_name}"

class Category(models.Model):
    """Model for categories monitered in profile.

    Args:
        models (django.model): .
    """
    category = models.CharField(max_length=50, primary_key=True)

    def __str__(self) -> str:
        return self.category