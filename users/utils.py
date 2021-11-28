from django.db.models import Q
from .models import Profile


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate(request, profiles, results):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, profiles


def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    profiles = Profile.objects.filter(role = 'Mental Health Specialist')

    profiles = profiles.filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query)
    )

    return profiles, search_query
