[app]
title = SprachSyntheseApp
package.name = sprache
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
source.exclude_dirs = tests
version = 0.1
requirements = python3,kivy,onnxruntime,numpy,sounddevice
android.permissions = INTERNET, RECORD_AUDIO

# Architektur festlegen
android.ndk = 25b
android.arch = armeabi-v7a, arm64-v8a
android.ndk_download_timeout = 1800
