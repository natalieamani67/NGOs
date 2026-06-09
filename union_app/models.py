from django.db import models

class WorkplaceIssue(models.Model):
    """Database table for tracking worker/client grievances and labor disputes."""
    reporter_name = models.CharField(max_length=150, verbose_name="Worker Full Name")
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    company_name = models.CharField(max_length=200, verbose_name="Employer/Company Name")
    issue_category = models.CharField(max_length=100, choices=[
        ('wages', 'Unpaid Wages / Underpayment'),
        ('dismissal', 'Unfair Dismissal / Termination'),
        ('safety', 'Occupational Safety/Health Hazard'),
        ('harassment', 'Workplace Harassment / Discrimination'),
        ('other', 'Other Labor Grievance')
    ], default='wages')
    incident_date = models.DateField(blank=True, null=True, verbose_name="Date of Incident")
    details = models.TextField(verbose_name="Detailed Description of the Issue")
    reported_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False, verbose_name="Mark as Resolved")

    def __str__(self):
        return f"Issue #{self.id} - {self.reporter_name} ({self.company_name})"

    class Meta:
        verbose_name = "Workplace Issue"
        verbose_name_plural = "Workplace Issues"


class UnionMember(models.Model):
    """Database table for tracking official, card-carrying union employees."""
    full_name = models.CharField(max_length=150)
    national_id = models.CharField(max_length=50, unique=True, verbose_name="National ID / Passport Number")
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    current_workplace = models.CharField(max_length=200, verbose_name="Current Factory / Employer")
    job_title = models.CharField(max_length=100, help_text="e.g., Machine Operator, Packer")
    date_employed = models.DateField(verbose_name="Employment Start Date")
    assigned_branch = models.CharField(max_length=50, choices=[
        ('Nairobi HQ', 'Nairobi Headquarters (Kilome Rd)'),
        ('Eldoret', 'Eldoret Branch'),
        ('Mombasa', 'Mombasa Branch'),
        ('Kisumu', 'Kisumu Branch'),
    ], default='Nairobi HQ')
    joined_at = models.DateTimeField(auto_now_add=True)
    membership_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending Verification'),
        ('active', 'Active Member'),
        ('suspended', 'Suspended')
    ], default='pending')

    def __str__(self):
        return f"{self.full_name} - ID: {self.national_id}"

    class Meta:
        verbose_name = "Union Member"
        verbose_name_plural = "Union Members"