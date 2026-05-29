from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PublishDiscoverySession"]

class PublishDiscoverySession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/PublishDiscoverySession"
    updatePublish = JavaMethod("(Landroid/net/wifi/aware/PublishConfig;)V")