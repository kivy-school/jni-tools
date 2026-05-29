from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdServicesPermissions"]

class AdServicesPermissions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdServicesPermissions"
    ACCESS_ADSERVICES_AD_ID = JavaStaticField("Ljava/lang/String;")
    ACCESS_ADSERVICES_AD_SELECTION = JavaStaticField("Ljava/lang/String;")
    ACCESS_ADSERVICES_ATTRIBUTION = JavaStaticField("Ljava/lang/String;")
    ACCESS_ADSERVICES_CUSTOM_AUDIENCE = JavaStaticField("Ljava/lang/String;")
    ACCESS_ADSERVICES_PROTECTED_SIGNALS = JavaStaticField("Ljava/lang/String;")
    ACCESS_ADSERVICES_TOPICS = JavaStaticField("Ljava/lang/String;")