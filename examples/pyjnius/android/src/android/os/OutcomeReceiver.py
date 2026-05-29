from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OutcomeReceiver"]

class OutcomeReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/OutcomeReceiver"
    onError = JavaMethod("(Ljava/lang/Throwable;)V")
    onResult = JavaMethod("(Ljava/lang/Object;)V")