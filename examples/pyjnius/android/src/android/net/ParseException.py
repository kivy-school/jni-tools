from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParseException"]

class ParseException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ParseException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]
    response = JavaField("Ljava/lang/String;")