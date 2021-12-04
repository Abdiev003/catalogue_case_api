from django.db import models

from products.models import Product


class Slider(models.Model):
    # relation's
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='slider')

    # information's
    image = models.ImageField(upload_to='slider/')

    # moderation's
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_id.name

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'
