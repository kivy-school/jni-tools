from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Observable"]

class Observable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Observable"
    __javaconstructor__ = [("()V", False)]
    addObserver = JavaMethod("(Ljava/util/Observer;)V")
    deleteObserver = JavaMethod("(Ljava/util/Observer;)V")
    notifyObservers = JavaMultipleMethod([("()V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    deleteObservers = JavaMethod("()V")
    setChanged = JavaMethod("()V")
    clearChanged = JavaMethod("()V")
    hasChanged = JavaMethod("()Z")
    countObservers = JavaMethod("()I")