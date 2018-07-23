# set the default Django settings module for the 'celery' program.
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'samplesdb.settings')
# Setup django project
django.setup()

from django.core.exceptions import ObjectDoesNotExist

from preps.models import AgressoProject, Project, NON_CORE_PROJECTS, CORE_PROJECTS

core_projects = AgressoProject.objects.using("agresso").raw(AgressoProject.core_view())
non_core_projects = AgressoProject.objects.using("agresso").raw(AgressoProject.non_core_view())

total_balance = lambda table, cost_code: AgressoProject.total_balance(table, cost_code)


for project in core_projects:
    try:
        proj_own = Project.objects.get(cost_code=project.cost_code)
        proj_own.balance_avail = total_balance(CORE_PROJECTS, project.cost_code)
        proj_own.is_core = True
        proj_own.save()
    except ObjectDoesNotExist:
        proj_own = Project(cost_code=project.cost_code,
                         balance_avail=total_balance(CORE_PROJECTS, project.cost_code),
                         is_core=True)
        proj_own.save()
        
for project in non_core_projects:
    try:
        proj_own = Project.objects.get(cost_code=project.cost_code)
        proj_own.balance_avail = total_balance(NON_CORE_PROJECTS, project.cost_code)
        proj_own.is_core = False
        proj_own.save()
    except ObjectDoesNotExist:
        proj_own = Project(cost_code=project.cost_code,
                         balance_avail=total_balance(NON_CORE_PROJECTS, project.cost_code),
                         is_core=False)
        proj_own.save()