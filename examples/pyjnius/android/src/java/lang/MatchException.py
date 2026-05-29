from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MatchException"]

class MatchException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/MatchException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]