from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EmptyStackException"]

class EmptyStackException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/EmptyStackException"
    __javaconstructor__ = [("()V", False)]