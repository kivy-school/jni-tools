from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSNotificationGenerationJob"]

class OSNotificationGenerationJob(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSNotificationGenerationJob"
    getNotification = JavaMethod("()Lcom/onesignal/OSNotification;")
    setNotification = JavaMethod("(Lcom/onesignal/OSNotification;)V")
    getContext = JavaMethod("()Landroid/content/Context;")
    setContext = JavaMethod("(Landroid/content/Context;)V")
    getJsonPayload = JavaMethod("()Lorg/json/JSONObject;")
    setJsonPayload = JavaMethod("(Lorg/json/JSONObject;)V")
    isRestoring = JavaMethod("()Z")
    setRestoring = JavaMethod("(Z)V")
    getShownTimeStamp = JavaMethod("()Ljava/lang/Long;")
    setShownTimeStamp = JavaMethod("(Ljava/lang/Long;)V")
    getOverriddenBodyFromExtender = JavaMethod("()Ljava/lang/CharSequence;")
    setOverriddenBodyFromExtender = JavaMethod("(Ljava/lang/CharSequence;)V")
    getOverriddenTitleFromExtender = JavaMethod("()Ljava/lang/CharSequence;")
    setOverriddenTitleFromExtender = JavaMethod("(Ljava/lang/CharSequence;)V")
    getOverriddenSound = JavaMethod("()Landroid/net/Uri;")
    setOverriddenSound = JavaMethod("(Landroid/net/Uri;)V")
    getOverriddenFlags = JavaMethod("()Ljava/lang/Integer;")
    setOverriddenFlags = JavaMethod("(Ljava/lang/Integer;)V")
    getOrgFlags = JavaMethod("()Ljava/lang/Integer;")
    setOrgFlags = JavaMethod("(Ljava/lang/Integer;)V")
    getOrgSound = JavaMethod("()Landroid/net/Uri;")
    setOrgSound = JavaMethod("(Landroid/net/Uri;)V")
    toString = JavaMethod("()Ljava/lang/String;")