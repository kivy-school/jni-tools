from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InterruptedException"]

class InterruptedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/InterruptedException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]