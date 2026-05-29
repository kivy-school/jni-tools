from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClassFormatError"]

class ClassFormatError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ClassFormatError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]