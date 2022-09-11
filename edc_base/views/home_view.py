from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .mixins import EdcBaseViewMixin
from django.conf import settings


class HomeView(EdcBaseViewMixin, TemplateView):

    template_name = 'edc_base/auth/login.html'
    navbar_name = 'edc_base'
    navbar_selected_item = 'edc_base'

    def get_context_data(self, **kwargs):
        from edc_base.freeze import edc_packages, third_party_packages
        context = super().get_context_data(**kwargs)
        context.update(
            edc_packages=edc_packages,
            third_party_packages=third_party_packages,
            installed_apps=settings.INSTALLED_APPS)
        return context
