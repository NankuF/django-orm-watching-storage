from django.utils.timezone import localtime

from datacenter.models import Visit
from django.shortcuts import render


def show_storage_information(request):
    visitors_in_storage = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visitor in visitors_in_storage:
        visitor.get_duration()
        non_closed_visits.append({'who_entered': visitor.passcard.owner_name,
                                  'entered_at': localtime(visitor.entered_at),
                                  'duration': visitor.format_duration(),
                                  'is_strange': visitor.is_visit_long()
                                  })

    visits = Visit.objects.all()
    long_visits = []
    for visit in visits:
        visit.get_duration()
        if visit.is_visit_long():
            long_visits.append(visit)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }

    return render(request, 'storage_information.html', context)
