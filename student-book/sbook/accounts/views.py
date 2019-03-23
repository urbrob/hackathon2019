from django.shortcuts import render
from django.http import Http404
from accounts.models import Group
from django.db.models import Q


def groups(request):
    my_groups = Group.objects.filter(users=request.user)
    all_groups = Group.objects.filter(~Q(users=request.user))
    return render(request, 'accounts/groups.html', {'my_groups': my_groups, 'all_groups': all_groups})
