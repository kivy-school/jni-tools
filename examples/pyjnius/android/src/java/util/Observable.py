from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Observable"]

class Observable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Observable"
    __javaconstructor__ = [("()V", False)]
    notifyObservers = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("()V", False, False)])
    addObserver = JavaMethod("(Ljava/util/Observer;)V")
    deleteObserver = JavaMethod("(Ljava/util/Observer;)V")
    deleteObservers = JavaMethod("()V")
    hasChanged = JavaMethod("()Z")
    countObservers = JavaMethod("()I")