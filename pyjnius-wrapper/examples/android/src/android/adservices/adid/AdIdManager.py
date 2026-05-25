from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdIdManager"]

class AdIdManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adid/AdIdManager"
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/adid/AdIdManager;")
    getAdId = JavaMultipleMethod([("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])