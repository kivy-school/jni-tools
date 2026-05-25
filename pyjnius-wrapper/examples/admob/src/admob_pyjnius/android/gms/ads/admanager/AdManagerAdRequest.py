from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdManagerAdRequest"]

class AdManagerAdRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/admanager/AdManagerAdRequest"
    getPublisherProvidedId = JavaMethod("()Ljava/lang/String;")
    getCustomTargeting = JavaMethod("()Landroid/os/Bundle;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/admanager/AdManagerAdRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Lcom/google/android/gms/ads/admanager/AdManagerAdRequest;")
        setPublisherProvidedId = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/admanager/AdManagerAdRequest$Builder;")
        addCategoryExclusion = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/admanager/AdManagerAdRequest$Builder;")
        self = JavaMethod("()Lcom/google/android/gms/ads/admanager/AdManagerAdRequest$Builder;")