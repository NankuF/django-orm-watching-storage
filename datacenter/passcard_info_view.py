from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    all_visits_with_passcard = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in all_visits_with_passcard:
        visit.get_duration()
        this_passcard_visits.append({'entered_at': localtime(visit.entered_at),
                                     'duration': visit.format_duration(),
                                     'is_strange': visit.is_visit_long()
                                     })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
