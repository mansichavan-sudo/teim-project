from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),

    # Lead URLs
    path('lead_form/', views.lead_form_view, name='lead_add'),
    path('lead_form/<int:pk>/', views.lead_form_view, name='lead_edit'),
    path('lead_delete/<int:pk>/', views.lead_delete_view, name='lead_delete'),

    # Product / Service URLs
    path('product_form/', views.product_form_view, name='product_add'),
    path('product_form/<int:pk>/', views.product_form_view, name='product_edit'),
    path('product_delete/<int:pk>/', views.product_delete_view, name='product_delete'),

    # Interaction URLs
    path('interaction_form/', views.interaction_form_view, name='interaction_add'),
    path('interaction_form/<int:pk>/', views.interaction_form_view, name='interaction_edit'),
    path('interaction_delete/<int:pk>/', views.interaction_delete_view, name='interaction_delete'),

    # Recommendation URLs
    path('recommendation_form/', views.recommendation_form_view, name='recommendation_add'),
    path('recommendation_form/<int:pk>/', views.recommendation_form_view, name='recommendation_edit'),
    path('recommendation_delete/<int:pk>/', views.recommendation_delete_view, name='recommendation_delete'),

    # Outcome URLs
    path('outcome_form/', views.outcome_form_view, name='outcome_add'),
    path('outcome_form/<int:pk>/', views.outcome_form_view, name='outcome_edit'),
    path('outcome_delete/<int:pk>/', views.outcome_delete_view, name='outcome_delete'),

    # ML Recommendation
    path('recommendation/', views.recommendation_view, name='ml_recommendation'),
    
]
