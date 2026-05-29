from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SubscribeDiscoverySession"]

class SubscribeDiscoverySession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/SubscribeDiscoverySession"
    updateSubscribe = JavaMethod("(Landroid/net/wifi/aware/SubscribeConfig;)V")