from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Observable"]

class Observable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/Observable"
    __javaconstructor__ = [("()V", False)]
    mObservers = JavaField("Ljava/util/ArrayList;")
    registerObserver = JavaMethod("(Ljava/lang/Object;)V")
    unregisterObserver = JavaMethod("(Ljava/lang/Object;)V")
    unregisterAll = JavaMethod("()V")