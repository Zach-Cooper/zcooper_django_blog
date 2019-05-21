from django.contrib import admin

from blogging.models import Post, Category

# Create an InlineModelAdmin to represent Categories on the Post admin view
class CategoryInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
            CategoryInline,
            ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    #Dont include "posts" field from the formin the Cat admin
    exclude = ('posts',)
