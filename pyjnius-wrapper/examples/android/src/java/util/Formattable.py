from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Formattable"]

class Formattable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Formattable"
    formatTo = JavaMethod("(Ljava/util/Formatter;III)V")