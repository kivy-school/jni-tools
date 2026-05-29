from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InstantiationError"]

class InstantiationError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/InstantiationError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]