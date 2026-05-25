from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InflateException"]

class InflateException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/InflateException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False)]