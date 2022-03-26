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

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
