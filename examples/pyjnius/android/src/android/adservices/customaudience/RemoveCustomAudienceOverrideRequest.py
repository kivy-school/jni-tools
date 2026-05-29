from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoveCustomAudienceOverrideRequest"]

class RemoveCustomAudienceOverrideRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/RemoveCustomAudienceOverrideRequest"
    __javaconstructor__ = [("(Landroid/adservices/common/AdTechIdentifier;Ljava/lang/String;)V", False)]
    getBuyer = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getName = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/RemoveCustomAudienceOverrideRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setBuyer = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/customaudience/RemoveCustomAudienceOverrideRequest$Builder;")
        setName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/customaudience/RemoveCustomAudienceOverrideRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/RemoveCustomAudienceOverrideRequest;")