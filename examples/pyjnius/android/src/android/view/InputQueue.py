from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputQueue"]

class InputQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/InputQueue"

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/InputQueue$Callback"
        onInputQueueCreated = JavaMethod("(Landroid/view/InputQueue;)V")
        onInputQueueDestroyed = JavaMethod("(Landroid/view/InputQueue;)V")