from django.shortcuts import render
from django.views import View

def EditResultViewClass(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'staff_templates/edit_result_template.html')
    def post(self, request, *args, **kwargs):
        pass