[app]
title = KivyAdMob
package.name = kivyadmob
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Python / Kivy
requirements = python3,kivy,pyjnius

# Android SDK / Build Tools
android.sdk_path = /usr/local/lib/android/sdk
android.sdk_version = 33
android.build_tools_version = 33.0.2

# Android permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# AdMob
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.6.0
android.manifest.application_meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-xxxxxxxxxxxxxxxx~yyyyyyyyyy

# UI
orientation = portrait
fullscreen = 0
