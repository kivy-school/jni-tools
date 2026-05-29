from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SdkExtensions"]

class SdkExtensions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ext/SdkExtensions"
    AD_SERVICES = JavaStaticField("I")
    getAllExtensionVersions = JavaStaticMethod("()Ljava/util/Map;")
    getExtensionVersion = JavaStaticMethod("(I)I")