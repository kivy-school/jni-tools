from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationConfiguration"]

class MediationConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationConfiguration"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/AdFormat;Landroid/os/Bundle;)V", False)]
    CUSTOM_EVENT_SERVER_PARAMETER_FIELD = JavaStaticField("Ljava/lang/String;")
    getFormat = JavaMethod("()Lcom/google/android/gms/ads/AdFormat;")
    getServerParameters = JavaMethod("()Landroid/os/Bundle;")