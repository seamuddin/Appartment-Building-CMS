from .models import GeneralSettings


def ct_processor(request):
    setting = GeneralSettings.objects.first()
    return {'setting': setting}
