from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdServicesOutcomeReceiver"]

class AdServicesOutcomeReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdServicesOutcomeReceiver"
    onError = JavaMethod("(Ljava/lang/Throwable;)V")
    onResult = JavaMethod("(Ljava/lang/Object;)V")