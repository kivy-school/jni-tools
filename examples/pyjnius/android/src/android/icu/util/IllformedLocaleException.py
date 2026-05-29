from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllformedLocaleException"]

class IllformedLocaleException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/IllformedLocaleException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;I)V", False), ("(Ljava/lang/String;)V", False)]
    getErrorIndex = JavaMethod("()I")