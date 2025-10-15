from django.db import models

# -----------------------------
# Lead Model
# -----------------------------
class Lead(models.Model):
    LEAD_TYPE_CHOICES = [
        ('Hot', 'Hot'),
        ('Warm', 'Warm'),
        ('Cold', 'Cold'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)  # optional
    lead_type = models.CharField(max_length=20, choices=LEAD_TYPE_CHOICES)

    def __str__(self):
        return self.name


# -----------------------------
# ServiceProduct Model
# -----------------------------
class ServiceProduct(models.Model):
    CATEGORY_CHOICES = [
        ('Product', 'Product'),
        ('Service', 'Service'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# -----------------------------
# LeadInteraction Model
# ----------------------------- 
class LeadInteraction(models.Model):
    INTERACTION_CHOICES = [
        ('Call', 'Call'),
        ('Email', 'Email'),
        ('Meeting', 'Meeting'),
    ]
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=20, choices=INTERACTION_CHOICES)
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # new field


# -----------------------------
# Recommendation Model
# -----------------------------
class Recommendation(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    service_product = models.ForeignKey(ServiceProduct, on_delete=models.CASCADE)
    recommendation_type = models.CharField(max_length=50, blank=True)  # optional type
    upsell_item = models.CharField(max_length=100, blank=True, default="")
    cross_sell_item = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return f"{self.lead.name} - {self.service_product.name}"


# -----------------------------
# RecommendationOutcome Model
# -----------------------------
class RecommendationOutcome(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    notes = models.TextField(blank=True)
    outcome = models.TextField()

    def __str__(self):
        return f"{self.lead.name} - Outcome"
