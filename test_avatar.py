#!/usr/bin/env python
"""
Test script to verify avatar upload functionality
"""
import os

import django

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# Django imports after setup
from django.contrib.auth.models import User  # noqa: E402
from django.core.files.uploadedfile import SimpleUploadedFile  # noqa: E402

from core.forms import AvatarUploadForm  # noqa: E402
from core.models import UserProfile  # noqa: E402


def test_avatar_upload():
    print("🧪 Testing Avatar Upload Functionality")
    print("=" * 50)

    # Get the test user 'guada'
    try:
        user = User.objects.get(username="guada")
        print(f"✅ Found user: {user.username} ({user.first_name})")
    except User.DoesNotExist:
        print("❌ User 'guada' not found")
        return

    # Get or create user profile
    profile, created = UserProfile.objects.get_or_create(user=user)
    print(f"📝 Profile created: {created}")
    print(f"📁 Current avatar: {profile.avatar}")

    # Use an existing image file for testing
    existing_image_path = r"C:\DjangoCourse\media\avatars\55a7ee4f-8f56-4866-8e98-2ee7009dd768.jpg"

    if os.path.exists(existing_image_path):
        print(f"📷 Using existing image: {existing_image_path}")
        with open(existing_image_path, "rb") as f:
            test_image = SimpleUploadedFile(
                name="test_avatar.jpg", content=f.read(), content_type="image/jpeg"
            )
    else:
        print("❌ No existing image found, creating simple test image")
        # Create a simple test image file
        test_image_content = (
            b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
            b"\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc```\x00\x00"
            b"\x00\x04\x00\x01\xdd\x8d\xb4\x1c\x00\x00\x00\x00IEND\xaeB`\x82"
        )
        test_image = SimpleUploadedFile(
            name="test_avatar.png", content=test_image_content, content_type="image/png"
        )

    # Test the form
    form_data = {}
    form_files = {"avatar": test_image}

    form = AvatarUploadForm(data=form_data, files=form_files, instance=profile)
    print(f"🔍 Form is valid: {form.is_valid()}")

    if form.is_valid():
        print("💾 Saving form...")
        saved_profile = form.save()
        print(f"✅ Avatar saved: {saved_profile.avatar}")
        print(f"📂 Avatar path: {saved_profile.avatar.path if saved_profile.avatar else 'None'}")
    else:
        print(f"❌ Form errors: {form.errors}")

    print("=" * 50)
    print("🏁 Test completed")


if __name__ == "__main__":
    test_avatar_upload()
