import os
import re

# Path to the root directory of your Django project
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# List of your Django apps
APPS = ['gifts',
    'wallet',
    'discover',
    'nearby',
    'party_room',
    'video_call',
    'bot',
    
    'moments',
    'follow',
    'location',
    'levels',]

# Function to generate admin.py content
def generate_admin_content(app_name, models):
    admin_content = "from django.contrib import admin\n"
    admin_content += f"from .models import {', '.join(models)}\n\n"

    for model in models:
        admin_content += f"@admin.register({model})\n"
        admin_content += f"class {model}Admin(admin.ModelAdmin):\n"
        admin_content += "    list_display = ('id',)\n"  # Default list_display
        admin_content += "    search_fields = ('id',)\n"  # Default search_fields
        admin_content += "\n"
    
    return admin_content

# Function to get models from models.py
def get_models(app_path):
    models = []
    models_file = os.path.join(app_path, 'models.py')
    if os.path.exists(models_file):
        with open(models_file, 'r') as file:
            content = file.read()
            models = re.findall(r'class (\w+)\(models.Model\):', content)
    return models

# Generate admin.py for each app
for app in APPS:
    app_path = os.path.join(PROJECT_ROOT, app)
    models = get_models(app_path)
    if models:
        admin_content = generate_admin_content(app, models)
        admin_file = os.path.join(app_path, 'admin.py')
        with open(admin_file, 'w') as file:
            file.write(admin_content)
        print(f"Generated admin.py for {app}")
    else:
        print(f"No models found for {app}")
