from django.db import models


class Members(models.Model):
    ROLE_CHOICES = [
        ('DEV', 'Developer'),
        ('TECH-LEAD', 'Technology Lead'),
        ('LEADER', 'IT Manager/Leader'),
        ('PM', 'Project Manager'),
        ('ANALYST', 'System Engineer'),
        ('PRODUCT-MANAGER', 'Product Manager'),
        ('TPM', 'Technical Program Manager'),
        ('SCRUM-MASTER', 'Scrum Master'),
        ('DS', 'Data Scientist'),
        ('QA', 'Quality Assurance'),
        ('UX', 'UX/UI Designer'),
        # Add other roles as needed
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField
    description = models.TextField()
    email = models.EmailField(unique=True, null=True)
    role = models.CharField(max_length=25, choices=ROLE_CHOICES, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='team_pics/', blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    twitter_x_url = models.URLField(blank=True, null=True)
    portfolio_name = models.CharField(max_length=200, null=True)
    core_pod_name = models.CharField(max_length=200, null=True)
    core_skill = models.CharField(max_length=200, null=True)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}  - {self.role}  - Portfolio:  {self.portfolio_name}  "
                f"- POD:  {self.core_pod_name}")

