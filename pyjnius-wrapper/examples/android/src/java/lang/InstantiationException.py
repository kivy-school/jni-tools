from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InstantiationException"]

class InstantiationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/InstantiationException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]