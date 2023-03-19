from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    categories = models.ManyToManyField(Category)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.reviewer_name} - {self.book.title}"
