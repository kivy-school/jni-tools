from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidPreferencesFormatException"]

class InvalidPreferencesFormatException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/prefs/InvalidPreferencesFormatException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]