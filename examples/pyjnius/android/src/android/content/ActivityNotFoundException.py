from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ActivityNotFoundException"]

class ActivityNotFoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ActivityNotFoundException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]