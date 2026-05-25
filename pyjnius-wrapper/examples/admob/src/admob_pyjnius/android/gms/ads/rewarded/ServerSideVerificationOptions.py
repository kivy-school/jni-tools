from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServerSideVerificationOptions"]

class ServerSideVerificationOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/rewarded/ServerSideVerificationOptions"
    getUserId = JavaMethod("()Ljava/lang/String;")
    getCustomData = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/rewarded/ServerSideVerificationOptions/Builder"
        __javaconstructor__ = [("()V", False)]
        setUserId = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/rewarded/ServerSideVerificationOptions$Builder;")
        setCustomData = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/rewarded/ServerSideVerificationOptions$Builder;")
        build = JavaMethod("()Lcom/google/android/gms/ads/rewarded/ServerSideVerificationOptions;")