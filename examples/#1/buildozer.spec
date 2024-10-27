[app]
title = SprachSyntheseApp
package.name = sprache
package.domain = org.example
source.dir = .
source.exclude_dirs = tests
version = 0.1

# Hier die ONNX-Datei mit einschließen
source.include_exts = py,png,jpg,kv,atlas,onnx
# Optional: Wenn dein Modell in einem bestimmten Verzeichnis liegt
source.include_patterns = assets/models/*.onnx
source.exclude_exts = spec

# Requirements
requirements = python3,kivy,onnxruntime,numpy,sounddevice,kivy_deps.sdl2,kivy_deps.glew

# Android spezifische Einstellungen
android.permissions = INTERNET, RECORD_AUDIO
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
android.ndk_download_timeout = 1800
android.gradle_version = 7.6.1
android.build_tools_version = 30.0.3
android.accept_sdk_license = True
android.skip_update = False
android.gradle_dependencies = org.jetbrains.kotlin:kotlin-stdlib:1.8.22
p4a.bootstrap = sdl2

log_level = 1
