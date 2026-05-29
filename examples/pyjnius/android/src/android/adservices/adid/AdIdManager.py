from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdIdManager"]

class AdIdManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adid/AdIdManager"
    getAdId = JavaMultipleMethod([("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/adid/AdIdManager;")