[app]

# (str) Title of your application
title = SmartAgricultureApp

# (str) Package name
package.name = smart_agriculture_app

# (str) Package domain (needed for Android/IOS packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = kivy, requests, numpy, opencv-python

# (str) Custom source folders for requirements
# Sets custom source folders for requirements
# requirements.source.kivy = ../../../kivy
# requirements.source.myreq = ../../myreq

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,CAMERA

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Target application architecture
arch = armeabi-v7a

# (str) Path to the android ndk for the current python-for-android release
# android.ndk_path = /opt/android-ndk-r19c

# (str) Android NDK version to use
# android.ndk = 19c

# (int) Android API to use
# android.api = 28

# (int) Minimum API required
# android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 20

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_path =

# (list) Application requirements
requirements = kivy, requests, numpy, opencv-python

# (str) Presplash of the application
presplash.filename = %(source.dir)/logo.png

# (str) Icon of the application
icon.filename = %(source.dir)/logo.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
# android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,CAMERA

# (list) Features (adds a comma-separated list of features available in the Android API, see
# https://developer.android.com/guide/topics/manifest/uses-feature-element.html
# android.features = android.hardware.usb.host

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (str) Android additional Gradle repositories to use
# android.gradle_dependencies = com.android.support:support-v4:27.1.1

# (list) Android Gradle dependencies to add
# android.gradle_dependencies = com.google.firebase:firebase-core:16.0.1

# (list) Android AAR dependencies to add (currently works only with sdl2_gradle
# android.gradle_aars = com.example.directory:library:1.0.0
