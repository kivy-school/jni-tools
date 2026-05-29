from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LogPrinter"]

class LogPrinter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/LogPrinter"
    __javaconstructor__ = [("(ILjava/lang/String;)V", False)]
    println = JavaMethod("(Ljava/lang/String;)V")