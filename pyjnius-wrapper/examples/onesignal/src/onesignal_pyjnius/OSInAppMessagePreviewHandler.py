from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInAppMessagePreviewHandler"]

class OSInAppMessagePreviewHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSInAppMessagePreviewHandler"
    INSTANCE = JavaStaticField("Lcom/onesignal/OSInAppMessagePreviewHandler;")
    notificationReceived = JavaStaticMethod("(Landroid/content/Context;Landroid/os/Bundle;)Z")
    notificationOpened = JavaStaticMethod("(Landroid/app/Activity;Lorg/json/JSONObject;)Z")
    inAppPreviewPushUUID = JavaStaticMethod("(Lorg/json/JSONObject;)Ljava/lang/String;")