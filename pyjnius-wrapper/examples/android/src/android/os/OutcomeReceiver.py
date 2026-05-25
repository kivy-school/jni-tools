from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OutcomeReceiver"]

class OutcomeReceiver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/OutcomeReceiver"
    onResult = JavaMethod("(Ljava/lang/Object;)V")
    onError = JavaMethod("(Ljava/lang/Throwable;)V")