from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdServicesOutcomeReceiver"]

class AdServicesOutcomeReceiver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdServicesOutcomeReceiver"
    onResult = JavaMethod("(Ljava/lang/Object;)V")
    onError = JavaMethod("(Ljava/lang/Throwable;)V")