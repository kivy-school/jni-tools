from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ICUUncheckedIOException"]

class ICUUncheckedIOException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/ICUUncheckedIOException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]