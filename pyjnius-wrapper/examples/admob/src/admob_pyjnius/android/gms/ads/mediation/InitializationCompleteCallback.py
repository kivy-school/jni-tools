from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InitializationCompleteCallback"]

class InitializationCompleteCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/InitializationCompleteCallback"
    onInitializationSucceeded = JavaMethod("()V")
    onInitializationFailed = JavaMethod("(Ljava/lang/String;)V")