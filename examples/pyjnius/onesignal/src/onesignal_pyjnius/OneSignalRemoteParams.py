from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OneSignalRemoteParams"]

class OneSignalRemoteParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OneSignalRemoteParams"
    __javaconstructor__ = [("()V", False)]
    DEFAULT_INDIRECT_ATTRIBUTION_WINDOW = JavaStaticField("I")
    DEFAULT_NOTIFICATION_LIMIT = JavaStaticField("I")

    class InfluenceParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignalRemoteParams/InfluenceParams"
        __javaconstructor__ = [("()V", False)]
        getIndirectNotificationAttributionWindow = JavaMethod("()I")
        getNotificationLimit = JavaMethod("()I")
        getIndirectIAMAttributionWindow = JavaMethod("()I")
        getIamLimit = JavaMethod("()I")
        isDirectEnabled = JavaMethod("()Z")
        isIndirectEnabled = JavaMethod("()Z")
        isUnattributedEnabled = JavaMethod("()Z")
        toString = JavaMethod("()Ljava/lang/String;")