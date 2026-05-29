from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConditionVariable"]

class ConditionVariable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ConditionVariable"
    __javaconstructor__ = [("()V", False), ("(Z)V", False)]
    close = JavaMethod("()V")
    open = JavaMethod("()V")
    block = JavaMultipleMethod([("()V", False, False), ("(J)Z", False, False)])