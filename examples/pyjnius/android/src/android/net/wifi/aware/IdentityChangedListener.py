from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IdentityChangedListener"]

class IdentityChangedListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/IdentityChangedListener"
    __javaconstructor__ = [("()V", False)]
    CLUSTER_CHANGE_EVENT_JOINED = JavaStaticField("I")
    CLUSTER_CHANGE_EVENT_STARTED = JavaStaticField("I")
    onIdentityChanged = JavaMethod("([B)V")
    onClusterIdChanged = JavaMethod("(ILandroid/net/MacAddress;)V")