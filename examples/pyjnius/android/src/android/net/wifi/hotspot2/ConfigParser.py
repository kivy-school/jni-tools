from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConfigParser"]

class ConfigParser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/hotspot2/ConfigParser"
    parsePasspointConfig = JavaStaticMethod("(Ljava/lang/String;[B)Landroid/net/wifi/hotspot2/PasspointConfiguration;")