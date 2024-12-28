from django.db.models import Q, F
from django.shortcuts import render

from .models.student import Student

from django.http import JsonResponse


# Create your views here.
def search_score(request):
    student = None
    error = None
    if request.method == "POST":
        reg_number = request.POST.get(
            'register_number')  # Match with form input's name attribute
        student = Student.objects.filter(sbd=reg_number).first()

        if not student:
            error = "No student found with the given registration number."

    return render(request, 'search_score.html',
                  {'student': student, 'error': error})


def dashboard(request):
    subjects = [["Math", 'toan'],
                ["Literature", 'ngu_van'],
                ["Foreign language", 'ngoai_ngu'],
                ["Physics", 'vat_ly'],
                ["Chemistry", 'hoa_hoc'],
                ["Biology", 'sinh_hoc'],
                ["Geography", 'dia_ly'],
                ["History", 'lich_su'],
                ["Civic Education", 'gdcd'],
                ]

    # Initialize statistics dictionary
    report_data = {}

    for title, subject in subjects:
        report_data[title] = {
            '>=8': Student.objects.filter(**{f"{subject}__gte": 8}).count(),
            '6-8': Student.objects.filter(Q(**{f"{subject}__gte": 6}) & Q(**{f"{subject}__lt": 8})).count(),
            '4-6': Student.objects.filter(Q(**{f"{subject}__gte": 4}) & Q(**{f"{subject}__lt": 6})).count(),
            '<4': Student.objects.filter(**{f"{subject}__lt": 4}).count(),
        }
    return render(request, 'dash_board.html', {'report_data': report_data})


def top_student(request):
    top_students = (
        Student.objects.exclude(
            toan__isnull=True,
            hoa_hoc__isnull=True,
            vat_ly__isnull=True,
        )
        .annotate(
            total_score=F("toan") + F("vat_ly") + F("hoa_hoc"))
        .order_by("-total_score")[:10]
    )
    return render(
        request,
        "top_student.html",
        {"students": top_students},
    )

