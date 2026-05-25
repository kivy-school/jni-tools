from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferencesFactory"]

class PreferencesFactory(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/prefs/PreferencesFactory"
    systemRoot = JavaMethod("()Ljava/util/prefs/Preferences;")
    userRoot = JavaMethod("()Ljava/util/prefs/Preferences;")