from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Other apps
    path('', include('crmapp.urls')),
    path('ocrapp/', include('ocrapp.urls')),
    path('open_ai/', include('open_ai.urls')),
    path('generate_quotation/', include('generate_quotation.urls')),
    path('email_sender/', include('email_sender.urls')),
    path('schedule_meetings/', include('schedule_meetings.urls')),
    path('generate_invoice/', include('generate_invoice.urls')),
    path("chat_app/", include("chat_app.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("ai-calling/", include("ai_calling.urls")),
    path("api/ai-calling/", include("ai_calling.api_urls")),

    # Lead Automation
    path('lead_automation/', include('lead_automation.urls')),

    #path('', include('lead_automation.urls')),  # ✅ Default root URLs for lead_automation
]
