# lead_automation/forms.py
from django import forms
from .models import Lead, ServiceProduct, LeadInteraction, Recommendation, RecommendationOutcome

# -----------------------------
# Lead Form
# -----------------------------
class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'contact_number', 'lead_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lead Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'lead_type': forms.Select(attrs={'class': 'form-select'}),
        }


# -----------------------------
# ServiceProduct Form
# -----------------------------
class ServiceProductForm(forms.ModelForm):
    class Meta:
        model = ServiceProduct
        fields = ['name', 'category', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product/Service Name'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
        }


# -----------------------------
# LeadInteraction Form
# -----------------------------
class LeadInteractionForm(forms.ModelForm):
    class Meta:
        model = LeadInteraction
        fields = ['lead', 'interaction_type', 'notes']
        widgets = {
            'lead': forms.Select(attrs={'class': 'form-select'}),
            'interaction_type': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Interaction Notes', 'rows': 3}),
        }


# -----------------------------
# Recommendation Form
# -----------------------------
class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['lead', 'service_product', 'upsell_item', 'cross_sell_item']
        widgets = {
            'lead': forms.Select(attrs={'class': 'form-select'}),
            'service_product': forms.Select(attrs={'class': 'form-select'}),
            'upsell_item': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Upsell Item'}),
            'cross_sell_item': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cross-sell Item'}),
        }


# -----------------------------
# RecommendationOutcome Form
# -----------------------------
class RecommendationOutcomeForm(forms.ModelForm):
    class Meta:
        model = RecommendationOutcome
        fields = ['lead', 'recommendation', 'outcome']
        widgets = {
            'lead': forms.Select(attrs={'class': 'form-select'}),
            'recommendation': forms.Select(attrs={'class': 'form-select'}),
            'outcome': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Outcome Notes', 'rows': 3}),
        }
