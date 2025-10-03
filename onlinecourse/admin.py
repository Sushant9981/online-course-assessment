from django.contrib import admin
# ✅ Import all required models
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


# ------------------------------
# Lesson inline for Course
# ------------------------------
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# ------------------------------
# Question & Choice admin setup
# ------------------------------
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]   # show choices inside question editing
    list_display = ['question_text', 'course', 'grade']   # ✅ fixed field names


# ------------------------------
# Register models
# ------------------------------
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
