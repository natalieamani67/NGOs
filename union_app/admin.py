from django.contrib import admin
from .models import WorkplaceIssue, UnionMember

@admin.register(WorkplaceIssue)
class WorkplaceIssueAdmin(admin.ModelAdmin):
    list_display = ('reporter_name', 'company_name', 'issue_category', 'reported_at', 'is_resolved')
    list_filter = ('issue_category', 'is_resolved', 'reported_at')
    search_fields = ('reporter_name', 'company_name', 'details')

@admin.register(UnionMember)
class UnionMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'national_id', 'current_workplace', 'assigned_branch', 'membership_status')
    list_filter = ('assigned_branch', 'membership_status', 'joined_at')
    search_fields = ('full_name', 'national_id', 'current_workplace')