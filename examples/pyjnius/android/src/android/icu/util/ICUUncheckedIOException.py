from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ICUUncheckedIOException"]

class ICUUncheckedIOException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/ICUUncheckedIOException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]