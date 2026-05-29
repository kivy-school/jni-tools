from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JoinCustomAudienceRequest"]

class JoinCustomAudienceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/JoinCustomAudienceRequest"
    getCustomAudience = JavaMethod("()Landroid/adservices/customaudience/CustomAudience;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/JoinCustomAudienceRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setCustomAudience = JavaMethod("(Landroid/adservices/customaudience/CustomAudience;)Landroid/adservices/customaudience/JoinCustomAudienceRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/JoinCustomAudienceRequest;")