from django.contrib import admin
from .models import Post
from .models import UserInformation

@admin.register(UserInformation)
class UserInformationAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'gender', 'fitness_goal', 'created_at')
    list_filter = ('gender', 'fitness_goal')
    search_fields = ('user__username', 'user__email', 'phone')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'age', 'gender', 'phone', 'address')
        }),
        ('Physical Information', {
            'fields': ('height', 'weight', 'fitness_goal')
        }),
        ('Medical Information', {
            'fields': ('medical_conditions',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

# Define a custom admin class to improve the admin interface for the Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on', 'updated_on')
    list_filter = ('status', 'created_on', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_on',)

# Register the Post model with the custom admin class
admin.site.register(Post, PostAdmin)
