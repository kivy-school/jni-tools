from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalMonitorStateException"]

class IllegalMonitorStateException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/IllegalMonitorStateException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]