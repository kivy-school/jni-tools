from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SharedPreferences"]

class SharedPreferences(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/SharedPreferences"
    edit = JavaMethod("()Landroid/content/SharedPreferences$Editor;")
    getAll = JavaMethod("()Ljava/util/Map;")
    getStringSet = JavaMethod("(Ljava/lang/String;Ljava/util/Set;)Ljava/util/Set;")
    registerOnSharedPreferenceChangeListener = JavaMethod("(Landroid/content/SharedPreferences$OnSharedPreferenceChangeListener;)V")
    unregisterOnSharedPreferenceChangeListener = JavaMethod("(Landroid/content/SharedPreferences$OnSharedPreferenceChangeListener;)V")
    getBoolean = JavaMethod("(Ljava/lang/String;Z)Z")
    getInt = JavaMethod("(Ljava/lang/String;I)I")
    getLong = JavaMethod("(Ljava/lang/String;J)J")
    getFloat = JavaMethod("(Ljava/lang/String;F)F")
    contains = JavaMethod("(Ljava/lang/String;)Z")
    getString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")

    class OnSharedPreferenceChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/SharedPreferences$OnSharedPreferenceChangeListener"
        onSharedPreferenceChanged = JavaMethod("(Landroid/content/SharedPreferences;Ljava/lang/String;)V")

    class Editor(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/SharedPreferences$Editor"
        remove = JavaMethod("(Ljava/lang/String;)Landroid/content/SharedPreferences$Editor;")
        putBoolean = JavaMethod("(Ljava/lang/String;Z)Landroid/content/SharedPreferences$Editor;")
        putInt = JavaMethod("(Ljava/lang/String;I)Landroid/content/SharedPreferences$Editor;")
        putLong = JavaMethod("(Ljava/lang/String;J)Landroid/content/SharedPreferences$Editor;")
        putFloat = JavaMethod("(Ljava/lang/String;F)Landroid/content/SharedPreferences$Editor;")
        clear = JavaMethod("()Landroid/content/SharedPreferences$Editor;")
        commit = JavaMethod("()Z")
        apply = JavaMethod("()V")
        putStringSet = JavaMethod("(Ljava/lang/String;Ljava/util/Set;)Landroid/content/SharedPreferences$Editor;")
        putString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/content/SharedPreferences$Editor;")