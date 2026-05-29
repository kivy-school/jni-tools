from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebTriggerInput"]

class WebTriggerInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/WebTriggerInput"
    __javaconstructor__ = [("(Landroid/net/Uri;Ljava/lang/String;[B)V", False)]
    getAppPackageName = JavaMethod("()Ljava/lang/String;")
    getDestinationUrl = JavaMethod("()Landroid/net/Uri;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getData = JavaMethod("()[B")