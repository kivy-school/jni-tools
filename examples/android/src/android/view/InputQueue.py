from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputQueue"]

class InputQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/InputQueue"
    finalize = JavaMethod("()V")

    class Callback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/InputQueue/Callback"
        onInputQueueCreated = JavaMethod("(Landroid/view/InputQueue;)V")
        onInputQueueDestroyed = JavaMethod("(Landroid/view/InputQueue;)V")