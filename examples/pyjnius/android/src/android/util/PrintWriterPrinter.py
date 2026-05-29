from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintWriterPrinter"]

class PrintWriterPrinter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/PrintWriterPrinter"
    __javaconstructor__ = [("(Ljava/io/PrintWriter;)V", False)]
    println = JavaMethod("(Ljava/lang/String;)V")