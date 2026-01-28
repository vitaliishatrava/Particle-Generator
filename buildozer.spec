[app]
title = KivyAdMob
package.name = kivyadmob
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy,pyjnius

android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.6.0
android.manifest.application_meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-xxxxxxxxxxxxxxxx~yyyyyyyyyy

orientation = portrait
fullscreen = 0
