from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Printer"]

class Printer(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Printer"
    println = JavaMethod("(Ljava/lang/String;)V")