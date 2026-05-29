from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceChangeEvent"]

class PreferenceChangeEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/prefs/PreferenceChangeEvent"
    __javaconstructor__ = [("(Ljava/util/prefs/Preferences;Ljava/lang/String;Ljava/lang/String;)V", False)]
    getNode = JavaMethod("()Ljava/util/prefs/Preferences;")
    getKey = JavaMethod("()Ljava/lang/String;")
    getNewValue = JavaMethod("()Ljava/lang/String;")