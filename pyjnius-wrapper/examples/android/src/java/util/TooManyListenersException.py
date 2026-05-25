from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TooManyListenersException"]

class TooManyListenersException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/TooManyListenersException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]