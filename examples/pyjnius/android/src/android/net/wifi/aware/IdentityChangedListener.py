from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IdentityChangedListener"]

class IdentityChangedListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/IdentityChangedListener"
    __javaconstructor__ = [("()V", False)]
    CLUSTER_CHANGE_EVENT_JOINED = JavaStaticField("I")
    CLUSTER_CHANGE_EVENT_STARTED = JavaStaticField("I")
    onClusterIdChanged = JavaMethod("(ILandroid/net/MacAddress;)V")
    onIdentityChanged = JavaMethod("([B)V")