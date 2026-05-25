from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringBuilderPrinter"]

class StringBuilderPrinter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/StringBuilderPrinter"
    __javaconstructor__ = [("(Ljava/lang/StringBuilder;)V", False)]
    println = JavaMethod("(Ljava/lang/String;)V")