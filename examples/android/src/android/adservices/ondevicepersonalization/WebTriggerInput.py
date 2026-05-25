from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebTriggerInput"]

class WebTriggerInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/WebTriggerInput"
    getDestinationUrl = JavaMethod("()Landroid/net/Uri;")
    getAppPackageName = JavaMethod("()Ljava/lang/String;")
    getData = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")