from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllformedLocaleException"]

class IllformedLocaleException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/IllformedLocaleException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;I)V", False)]
    getErrorIndex = JavaMethod("()I")