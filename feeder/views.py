from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404

from feeder.models import Member


def home(request):
    tag = request.GET.get('tag', None)
    if tag:
        members = Member.objects.filter(tags__name__in=[tag])
    else:
        members = Member.objects.all()
    context = {
        'members': members,
        'tag': tag,
    }
    return render(request, 'home.html', context)


def detail(request, slug):
    member = get_object_or_404(Member, slug=slug)
    context = {
        'member': member,
    }
    return render(request, 'detail.html', context)


@csrf_exempt
def preview_rst(request):
    context = {
        'content': request.body,
    }
    return render(request, "preview_rst.html", context)
