from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintStreamPrinter"]

class PrintStreamPrinter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/PrintStreamPrinter"
    __javaconstructor__ = [("(Ljava/io/PrintStream;)V", False)]
    println = JavaMethod("(Ljava/lang/String;)V")