# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Achievements(models.Model):
    achievement_id = models.AutoField(primary_key=True)
    report = models.ForeignKey('Progressreports', models.DO_NOTHING, blank=True, null=True)
    achievement_description = models.TextField(blank=True, null=True)
    achievement_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Achievements'


class CaadStaff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CAAD_Staff'


class NcpEmployees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NCP_Employees'


class Progressreports(models.Model):
    report_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(NcpEmployees, models.DO_NOTHING, blank=True, null=True)
    report_date = models.DateField(blank=True, null=True)
    submited_by = models.ForeignKey(CaadStaff, models.DO_NOTHING, db_column='submited_by', blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProgressReports'


class Projectmilestones(models.Model):
    milestone_id = models.AutoField(primary_key=True)
    report = models.ForeignKey(Progressreports, models.DO_NOTHING, blank=True, null=True)
    milestone_description = models.TextField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProjectMilestones'


class Researchpublications(models.Model):
    publication_id = models.AutoField(primary_key=True)
    report = models.ForeignKey(Progressreports, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    journal = models.CharField(max_length=255, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    impact_factor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ResearchPublications'


class Supervision(models.Model):
    supervision_id = models.AutoField(primary_key=True)
    report = models.ForeignKey(Progressreports, models.DO_NOTHING, blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    thesis_topic = models.TextField(blank=True, null=True)
    supervision_start_date = models.DateField(blank=True, null=True)
    supervision_end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Supervision'


class Visits(models.Model):
    visit_id = models.AutoField(primary_key=True)
    report = models.ForeignKey(Progressreports, models.DO_NOTHING, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    visit_purpose = models.TextField(blank=True, null=True)
    visit_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Visits'
