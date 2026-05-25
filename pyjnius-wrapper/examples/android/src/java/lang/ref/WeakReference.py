from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WeakReference"]

class WeakReference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/WeakReference"
    __javaconstructor__ = [("(Ljava/lang/Object;)V", False), ("(Ljava/lang/Object;Ljava/lang/ref/ReferenceQueue;)V", False)]