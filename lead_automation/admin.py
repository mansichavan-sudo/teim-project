from django.contrib import admin
from .models import Lead, ServiceProduct, LeadInteraction, Recommendation, RecommendationOutcome

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact_number', 'lead_type']
    list_filter = ['lead_type']
    search_fields = ['name', 'email', 'contact_number']
    ordering = ['name']


@admin.register(ServiceProduct)
class ServiceProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['name']


@admin.register(LeadInteraction)
class LeadInteractionAdmin(admin.ModelAdmin):
    list_display = ['lead', 'interaction_type', 'date', 'notes']
    list_filter = ['interaction_type', 'date']
    search_fields = ['lead__name', 'notes']
    ordering = ['date']


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ['lead', 'service_product', 'recommendation_type', 'upsell_item', 'cross_sell_item']
    list_filter = ['recommendation_type']
    search_fields = ['lead__name', 'service_product__name', 'upsell_item', 'cross_sell_item']
    ordering = ['lead']


@admin.register(RecommendationOutcome)
class RecommendationOutcomeAdmin(admin.ModelAdmin):
    list_display = ['lead', 'recommendation', 'status', 'notes', 'outcome']
    list_filter = ['status']
    search_fields = ['lead__name', 'recommendation__service_product__name', 'notes', 'outcome']
    ordering = ['lead']
