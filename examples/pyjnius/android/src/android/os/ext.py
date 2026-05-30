from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SdkExtensions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ext/SdkExtensions"
    AD_SERVICES = JavaStaticField("I")
    getExtensionVersion = JavaStaticMethod("(I)I")
    getAllExtensionVersions = JavaStaticMethod("()Ljava/util/Map;")