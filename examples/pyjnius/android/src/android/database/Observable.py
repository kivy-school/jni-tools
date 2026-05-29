from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Observable"]

class Observable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/Observable"
    __javaconstructor__ = [("()V", False)]
    unregisterObserver = JavaMethod("(Ljava/lang/Object;)V")
    unregisterAll = JavaMethod("()V")
    registerObserver = JavaMethod("(Ljava/lang/Object;)V")