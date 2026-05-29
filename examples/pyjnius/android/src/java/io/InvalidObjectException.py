from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidObjectException"]

class InvalidObjectException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/InvalidObjectException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]