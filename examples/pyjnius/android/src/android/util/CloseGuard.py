from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CloseGuard"]

class CloseGuard(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/CloseGuard"
    __javaconstructor__ = [("()V", False)]
    warnIfOpen = JavaMethod("()V")
    close = JavaMethod("()V")
    open = JavaMethod("(Ljava/lang/String;)V")