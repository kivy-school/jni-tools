from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSSMSSubscriptionObserver"]

class OSSMSSubscriptionObserver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSSMSSubscriptionObserver"
    onSMSSubscriptionChanged = JavaMethod("(Lcom/onesignal/OSSMSSubscriptionStateChanges;)V")