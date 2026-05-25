from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceChangeListener"]

class PreferenceChangeListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/prefs/PreferenceChangeListener"
    preferenceChange = JavaMethod("(Ljava/util/prefs/PreferenceChangeEvent;)V")