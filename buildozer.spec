[app]

title = Tareq - The Red Thread
package.name = tareqredthread
package.domain = com.tareqomairi

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,wav

version = 1.0.0

requirements = python3,kivy

orientation = landscape
fullscreen = 1

android.api = 36
android.minapi = 24
android.ndk = 28c
android.archs = arm64-v8a
android.accept_sdk_license = True

# Ubuntu 24.04 / Python 3.12 debug-build path.
# p4a master is the stable line for Python <= 3.12.
p4a.branch = master

[buildozer]

log_level = 2
warn_on_root = 1
