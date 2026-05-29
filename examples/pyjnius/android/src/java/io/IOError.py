from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IOError"]

class IOError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/IOError"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False)]