from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Formattable"]

class Formattable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Formattable"
    formatTo = JavaMethod("(Ljava/util/Formatter;III)V")