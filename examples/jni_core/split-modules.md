
kivy-garden got this system 
where each component has same root folder and it will just merge them into that when pip installing a component


https://pypi.org/project/kivy-garden.matplotlib/


kivy_garden.matplotlib-0.1.1.dev0/
```
.
├── AUTHORS.txt
├── LICENSE.txt
├── PKG-INFO
├── README.md
├── kivy_garden
│   └── matplotlib
│       ├── __init__.py
│       ├── _version.py
│       ├── backend_kivy.py
│       ├── backend_kivyagg.py
│       └── tests
│           ├── __init__.py
│           ├── test_backend_kivy.py
│           ├── test_backend_kivyagg.py
│           └── test_events.py
├── kivy_garden.matplotlib.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── requires.txt
│   └── top_level.txt
├── setup.cfg
└── setup.py

5 directories, 19 files
```

soo dont see how this should not be possible to work by:
* android.android (android/android)
* android.dalvik (android/dalvik)
* android.java (android/java)
* android.javax (android/javax)
* android.org (android/org)



and now android.android (android/android)

get splitted into

android.accounts (android/android/accounts)
android.animation (android/android/animation)
android.content (android/android/content)
android.gesture (android/android/gesture)
android.heath (android/android/health)
android.text (android/android/text)

only android.android needs to work like this
android.android[accounts]
android.android[text]

i assume we can just make some pip shell for android.android
and under it , it has sub_packages which android.android[group_name] will trigger 
and each sub_package just has the android/android/<name> structure..

soo deps for some android python app would be like

```toml
dependencies = [
    "android.java",
    "android.org",
    "android.android[bluetooth]",
    "android.android[text]"
]
```

