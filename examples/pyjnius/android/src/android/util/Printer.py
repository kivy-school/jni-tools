from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Printer"]

class Printer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Printer"
    println = JavaMethod("(Ljava/lang/String;)V")