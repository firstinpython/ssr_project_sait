from django.shortcuts import render

# Create your view here.

def project(request, project_id):
    context = {
        'project_id':project_id
    }
    return render(request,'projects/project.html',context=context)