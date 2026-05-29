from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnsupportedClassVersionError"]

class UnsupportedClassVersionError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/UnsupportedClassVersionError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]