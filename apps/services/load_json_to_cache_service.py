import os
import json
from django.core.cache import cache
from django.conf import settings


def load_and_cache_json_data(file_path):
    # Construct the absolute file path based on the file name
    absolute_file_path = os.path.join(settings.MEDIA_ROOT, file_path)

    try:
        with open(absolute_file_path, 'r') as f:
            json_data = json.load(f)
            cache.set(file_path, json_data)
    except FileNotFoundError:
        cache.set(file_path, [])
