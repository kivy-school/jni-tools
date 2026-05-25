from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArrayStoreException"]

class ArrayStoreException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ArrayStoreException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]