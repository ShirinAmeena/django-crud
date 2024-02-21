from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    mark1 = models.IntegerField()
    mark2 = models.IntegerField()
    mark3 = models.IntegerField()

    def __str__(self):
        return self.student_name

    def total_marks(self):
        return self.mark1 + self.mark2 + self.mark3

    def result(self):
        if self.mark1 >= 35 and self.mark2 >= 35 and self.mark3 >= 35 and self.total_marks() >= 120:
            return 'PASSED'
        else:
            return 'FAILED'

    def grade(self):
        total_marks = self.total_marks()
        if self.result() == 'PASSED':
            if total_marks >= 240:
                return 'OUTSTANDING'
            elif total_marks >= 180:
                return 'EXCELLENT'
            elif total_marks >= 150:
                return 'GOOD'
            else:
                return 'AVERAGE'
        else:
            return ''  # If the student failed, grade is not applicable