from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidClassException"]

class InvalidClassException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/InvalidClassException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False)]
    classname = JavaField("Ljava/lang/String;")
    getMessage = JavaMethod("()Ljava/lang/String;")