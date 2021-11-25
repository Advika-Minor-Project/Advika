from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateTracks(request, tracks, results):

    page = request.GET.get('page')
    paginator = Paginator(tracks, results)

    try:
        tracks = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        tracks = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        tracks = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, tracks
