from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FilterWriter"]

class FilterWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FilterWriter"
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("([CII)V", False, False), ("(I)V", False, False), ("(Ljava/lang/String;II)V", False, False)])