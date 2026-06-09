from django.shortcuts import render, redirect
from django.contrib import messages
from .models import WorkplaceIssue, UnionMember


def home_view(request):
    return render(request, 'union_app/home.html')


def about_view(request):
    return render(request, 'union_app/about.html')


def branches_view(request):
    return render(request, 'union_app/branches.html')


def report_issue_view(request):
    """Processes worker labor dispute submissions."""
    if request.method == 'POST':
        WorkplaceIssue.objects.create(
            reporter_name=request.POST.get('reporter_name'),
            phone_number=request.POST.get('phone_number'),
            email=request.POST.get('email'),
            company_name=request.POST.get('company_name'),
            issue_category=request.POST.get('issue_category'),
            incident_date=request.POST.get('incident_date') or None,
            details=request.POST.get('details')
        )
        messages.success(request,
                         "Your issue has been safely logged in the system. A union legal representative will review it.")
        return redirect('report_issue')

    return render(request, 'union_app/report_issue.html')


def member_signup_view(request):
    """Processes new member registration files."""
    if request.method == 'POST':
        national_id = request.POST.get('national_id')

        # Security validation: Prevent duplicate entry errors crashing the database
        if UnionMember.objects.filter(national_id=national_id).exists():
            messages.error(request, "A member with this National ID number is already registered.")
            return redirect('member_signup')

        UnionMember.objects.create(
            full_name=request.POST.get('full_name'),
            national_id=national_id,
            phone_number=request.POST.get('phone_number'),
            email=request.POST.get('email'),
            current_workplace=request.POST.get('current_workplace'),
            job_title=request.POST.get('job_title'),
            date_employed=request.POST.get('date_employed'),
            assigned_branch=request.POST.get('assigned_branch')
        )
        messages.success(request,
                         "Registration successful! Your digital credentials have been saved. Your membership status is: Pending Verification.")
        return redirect('member_signup')

    return render(request, 'union_app/member_signup.html')