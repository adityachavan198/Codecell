import os
from django.shortcuts import render
from django.views import View


class Codequestion(View):
    template_name = "Hackathon/code.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        code = request.POST.get('code')
        print(code)
        current_path = os.path.dirname(__file__)
        required_path = current_path + "/Code/code.py"
        f = open(required_path, "w+")
        f.write(code)
        f.close()
        command = 'python3 ' + required_path + ' > ' + current_path + "/Code/" + 'out_file.txt'
        os.system(command)
        return render(request, self.template_name, {})

