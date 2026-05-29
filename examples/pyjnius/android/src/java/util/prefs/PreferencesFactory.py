from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferencesFactory"]

class PreferencesFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/prefs/PreferencesFactory"
    userRoot = JavaMethod("()Ljava/util/prefs/Preferences;")
    systemRoot = JavaMethod("()Ljava/util/prefs/Preferences;")