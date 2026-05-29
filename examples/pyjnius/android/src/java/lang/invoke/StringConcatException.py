from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringConcatException"]

class StringConcatException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/StringConcatException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]