from django.db import models



    # slug = models.SlugField(unique=True)


    # def __str__(self):
    #     return self.slug
    #
    # def get_absolute_url(self):
    #     return reverse('shop:product_detail', kwargs={'slug': self.slug})
    #
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)