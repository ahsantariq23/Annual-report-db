from django.db import models

class NCPEmployee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class CAADStaff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class ProgressReport(models.Model):
    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Reviewed', 'Reviewed'),
        ('Approved', 'Approved'),
    ]
    
    employee = models.ForeignKey(NCPEmployee, on_delete=models.CASCADE)
    report_date = models.DateField()
    submitted_by = models.ForeignKey(CAADStaff, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Report {self.id} by {self.employee.name}"

class ResearchPublication(models.Model):
    report = models.ForeignKey(ProgressReport, on_delete=models.CASCADE, related_name='publications')
    title = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    publication_date = models.DateField()
    impact_factor = models.DecimalField(max_digits=4, decimal_places=3)

    def __str__(self):
        return self.title

class ProjectMilestone(models.Model):
    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    ]
    
    report = models.ForeignKey(ProgressReport, on_delete=models.CASCADE, related_name='milestones')
    milestone_description = models.TextField()
    completion_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Milestone {self.id} for {self.report.employee.name}"

class Visit(models.Model):
    report = models.ForeignKey(ProgressReport, on_delete=models.CASCADE, related_name='visits')
    location = models.CharField(max_length=200)
    visit_purpose = models.TextField()
    visit_date = models.DateField()

    def __str__(self):
        return f"Visit to {self.location} on {self.visit_date}"

class Supervision(models.Model):
    report = models.ForeignKey(ProgressReport, on_delete=models.CASCADE, related_name='supervisions')
    student_name = models.CharField(max_length=200)
    thesis_topic = models.TextField()
    supervision_start_date = models.DateField()
    supervision_end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Supervision of {self.student_name}"

class Achievement(models.Model):
    report = models.ForeignKey(ProgressReport, on_delete=models.CASCADE, related_name='achievements')
    achievement_description = models.TextField()
    achievement_date = models.DateField()

    def __str__(self):
        return f"Achievement on {self.achievement_date}"
