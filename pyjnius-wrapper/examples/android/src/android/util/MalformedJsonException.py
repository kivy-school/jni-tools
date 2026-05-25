from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MalformedJsonException"]

class MalformedJsonException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/MalformedJsonException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]