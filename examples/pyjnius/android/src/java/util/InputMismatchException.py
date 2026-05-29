from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputMismatchException"]

class InputMismatchException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/InputMismatchException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]