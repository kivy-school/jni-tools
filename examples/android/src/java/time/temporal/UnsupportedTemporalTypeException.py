from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnsupportedTemporalTypeException"]

class UnsupportedTemporalTypeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/UnsupportedTemporalTypeException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]