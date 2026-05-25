from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSEmailSubscriptionObserver"]

class OSEmailSubscriptionObserver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSEmailSubscriptionObserver"
    onOSEmailSubscriptionChanged = JavaMethod("(Lcom/onesignal/OSEmailSubscriptionStateChanges;)V")