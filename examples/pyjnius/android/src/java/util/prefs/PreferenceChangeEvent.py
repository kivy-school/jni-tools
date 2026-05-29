from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceChangeEvent"]

class PreferenceChangeEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/prefs/PreferenceChangeEvent"
    __javaconstructor__ = [("(Ljava/util/prefs/Preferences;Ljava/lang/String;Ljava/lang/String;)V", False)]
    getNewValue = JavaMethod("()Ljava/lang/String;")
    getKey = JavaMethod("()Ljava/lang/String;")
    getNode = JavaMethod("()Ljava/util/prefs/Preferences;")