import os
import pickle
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import Lead, ServiceProduct, LeadInteraction, Recommendation, RecommendationOutcome
from .forms import LeadForm, ServiceProductForm, LeadInteractionForm, RecommendationForm, RecommendationOutcomeForm

# ===========================
# ML Models
# ===========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPS_MODEL_PATH = os.path.join(BASE_DIR, "upsell_model.pkl")
CROSS_MODEL_PATH = os.path.join(BASE_DIR, "cross_model.pkl")

if os.path.exists(UPS_MODEL_PATH) and os.path.getsize(UPS_MODEL_PATH) > 0:
    with open(UPS_MODEL_PATH, "rb") as f:
        upsell_model, le_upsell, le_lead, le_service = pickle.load(f)
else:
    upsell_model = le_upsell = le_lead = le_service = None

if os.path.exists(CROSS_MODEL_PATH) and os.path.getsize(CROSS_MODEL_PATH) > 0:
    with open(CROSS_MODEL_PATH, "rb") as f:
        cross_model, le_cross, _, _ = pickle.load(f)
else:
    cross_model = le_cross = None

# ===========================
# Email Automation
# ===========================
def send_email(subject, recipient, template_name, context):
    html_message = render_to_string(template_name, context)
    plain_message = strip_tags(html_message)
    email = EmailMultiAlternatives(
        subject=subject,
        body=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[recipient]
    )
    email.attach_alternative(html_message, "text/html")
    email.send()

# ===========================
# Dashboard
# ===========================
def dashboard_view(request):
    context = {
        'leads': Lead.objects.all(),
        'products': ServiceProduct.objects.all(),
        'interactions': LeadInteraction.objects.all(),
        'recommendations': Recommendation.objects.all(),
        'outcomes': RecommendationOutcome.objects.all(),
    }
    return render(request, 'lead_automation/dashboard.html', context)

# ===========================
# Lead Views
# ===========================
def lead_form_view(request, pk=None):
    instance = get_object_or_404(Lead, pk=pk) if pk else None
    form = LeadForm(request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'lead_automation/lead_form.html', {'form': form})

def lead_delete_view(request, pk):
    get_object_or_404(Lead, pk=pk).delete()
    return redirect('dashboard')

# ===========================
# Product / Service Views
# ===========================
def product_form_view(request, pk=None):
    instance = get_object_or_404(ServiceProduct, pk=pk) if pk else None
    form = ServiceProductForm(request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'lead_automation/service_product_form.html', {'form': form})

def product_delete_view(request, pk):
    get_object_or_404(ServiceProduct, pk=pk).delete()
    return redirect('dashboard')

# ===========================
# Interaction Views
# ===========================
def interaction_form_view(request, pk=None):
    instance = get_object_or_404(LeadInteraction, pk=pk) if pk else None
    form = LeadInteractionForm(request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'lead_automation/interaction_form.html', {'form': form})

def interaction_delete_view(request, pk):
    get_object_or_404(LeadInteraction, pk=pk).delete()
    return redirect('dashboard')

# ===========================
# Recommendation Views
# ===========================
def recommendation_form_view(request, pk=None):
    instance = get_object_or_404(Recommendation, pk=pk) if pk else None
    form = RecommendationForm(request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'lead_automation/recommendation_form.html', {'form': form})

def recommendation_delete_view(request, pk):
    get_object_or_404(Recommendation, pk=pk).delete()
    return redirect('dashboard')

# ===========================
# Outcome Views
# ===========================
def outcome_form_view(request, pk=None):
    instance = get_object_or_404(RecommendationOutcome, pk=pk) if pk else None
    form = RecommendationOutcomeForm(request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'lead_automation/outcome_form.html', {'form': form})

def outcome_delete_view(request, pk):
    get_object_or_404(RecommendationOutcome, pk=pk).delete()
    return redirect('dashboard')

# ===========================
# ML Recommendation View
# =========================== 
# ===========================
# ML Recommendation View
# ===========================
import pandas as pd

def recommendation_view(request):
    recommendation = None

    le_lead_list = le_lead.classes_ if le_lead else ["Hot", "Warm", "Cold", "Not Interested", "Close Win", "Close Loss"]
    le_service_list = le_service.classes_ if le_service else ["Service", "Product"]

    if request.method == "POST":
        lead_type = request.POST.get("lead_type")
        service_type = request.POST.get("service_type")
        past_interactions = int(request.POST.get("past_interactions", 0))

        try:
            if upsell_model and cross_model:
                # Handle unseen labels safely
                lead_enc = le_lead.transform([lead_type])[0] if lead_type in le_lead.classes_ else -1
                service_enc = le_service.transform([service_type])[0] if service_type in le_service.classes_ else -1

                # Prepare dataframe with same feature names as during training
                X_test = pd.DataFrame([{
                    'lead_type': lead_enc,
                    'service_type': service_enc,
                    'past_interactions': past_interactions
                }])

                # Upsell prediction
                ups_pred = le_upsell.inverse_transform(upsell_model.predict(X_test))[0]

                # Cross-sell prediction
                cross_pred = le_cross.inverse_transform(cross_model.predict(X_test))[0]

                recommendation = {"upsell": ups_pred, "cross_sell": cross_pred}
            else:
                recommendation = {"upsell": "N/A", "cross_sell": "N/A"}
        except Exception as e:
            print("Prediction Error:", e)
            recommendation = {"upsell": "N/A", "cross_sell": "N/A"}

    return render(request, "lead_automation/recommendation.html", {
        "recommendation": recommendation,
        "le_lead_classes": le_lead_list,
        "le_service_classes": le_service_list
    })
