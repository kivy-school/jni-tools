from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PpsMoParser"]

class PpsMoParser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/hotspot2/omadm/PpsMoParser"
    parseMoText = JavaStaticMethod("(Ljava/lang/String;)Landroid/net/wifi/hotspot2/PasspointConfiguration;")