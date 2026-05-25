from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSSubscriptionObserver"]

class OSSubscriptionObserver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSSubscriptionObserver"
    onOSSubscriptionChanged = JavaMethod("(Lcom/onesignal/OSSubscriptionStateChanges;)V")