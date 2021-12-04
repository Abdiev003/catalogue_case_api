from django.db import models


class Category(models.Model):
    # information's
    name = models.CharField(max_length=50, db_index=True)
    description = models.TextField(blank=True)

    # moderation's
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    # relation's
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    # information's
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_favorite = models.BooleanField(default=False)

    # moderation's
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'