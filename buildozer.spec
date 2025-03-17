[app]
title = MyApp
package.name = sysdia
package.domain = org.kanaka
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

android.api = 34  # Change from 31 to 34
android.minapi = 21
android.sdk = 34
android.ndk = 23b
android.ndk_api = 21
android.build_tools_version = 34.0.0  # Force Build Tools 34.0.0

android.gradle_dependencies = com.android.tools.build:gradle:7.2.2
android.bootstrap = sdl2
android.arch = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True  # Force SDK License Acceptance
