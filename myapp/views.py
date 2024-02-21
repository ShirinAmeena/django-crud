from django.shortcuts import render, redirect,get_object_or_404
from .models import Student
# Create your views here.
def index(request):
    return render(request,'index.html')

def list(request):
    # Fetch all students from the database
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})
def student(request):
    if request.method == 'POST':
        student_name = request.POST['studentName']
        mark1 = request.POST['mark1']
        mark2 = request.POST['mark2']
        mark3 = request.POST['mark3']
        
        # Save data to the database
        student = Student.objects.create(
            student_name=student_name,
            mark1=mark1,
            mark2=mark2,
            mark3=mark3
        )
        student.save()

        # Redirect to a success page or wherever you want
        return redirect('list')  # Change 'success_page' to the name of your success page URL pattern

    return render(request, 'student.html') 

def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.student_name = request.POST['studentName']
        student.mark1 = request.POST['mark1']
        student.mark2 = request.POST['mark2']
        student.mark3 = request.POST['mark3']
        student.save()
        return redirect('list')  # Redirect back to the list view after editing
    return render(request, 'editstudent.html', {'student': student})

def delete_student(request, student_id):
    if request.method == 'GET':
        student = Student.objects.get(pk=student_id)
        student.delete()
        return redirect('list')  # Redirect to the list view after deletion
    else:
        # Handle other request methods if necessary
        pass