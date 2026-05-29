from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventUrlProvider"]

class EventUrlProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/EventUrlProvider"
    createEventTrackingUrlWithResponse = JavaMethod("(Landroid/os/PersistableBundle;[BLjava/lang/String;)Landroid/net/Uri;")
    createEventTrackingUrlWithRedirect = JavaMethod("(Landroid/os/PersistableBundle;Landroid/net/Uri;)Landroid/net/Uri;")