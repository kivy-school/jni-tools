from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Base64DataException"]

class Base64DataException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Base64DataException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]