from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CloseGuard"]

class CloseGuard(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/CloseGuard"
    __javaconstructor__ = [("()V", False)]
    open = JavaMethod("(Ljava/lang/String;)V")
    close = JavaMethod("()V")
    warnIfOpen = JavaMethod("()V")