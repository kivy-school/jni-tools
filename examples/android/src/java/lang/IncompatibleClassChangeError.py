from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IncompatibleClassChangeError"]

class IncompatibleClassChangeError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/IncompatibleClassChangeError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]