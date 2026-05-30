from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AdIdManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adid/AdIdManager"
    getAdId = JavaMultipleMethod([("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/adid/AdIdManager;")

class AdId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adid/AdId"
    __javaconstructor__ = [("(Ljava/lang/String;Z)V", False)]
    ZERO_OUT = JavaStaticField("Ljava/lang/String;")
    getAdId = JavaMethod("()Ljava/lang/String;")
    isLimitAdTrackingEnabled = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")