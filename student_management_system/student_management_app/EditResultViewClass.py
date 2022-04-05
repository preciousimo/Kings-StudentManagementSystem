from django.shortcuts import render
from django.views import View
from student_management_app.Forms import EditResultForm

class EditResultViewClass(View):
    def get(self, request, *args, **kwargs):
        staff_id = request.user.id
        edit_result_form = EditResultForm(staff_id=staff_id)
        return render(request, 'staff_templates/edit_result_template.html', {'form':edit_result_form})

    def post(self, request, *args, **kwargs):
        pass