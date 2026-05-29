from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FederatedComputeInput"]

class FederatedComputeInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/FederatedComputeInput"
    getPopulationName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/FederatedComputeInput$Builder"
        __javaconstructor__ = [("()V", False)]
        setPopulationName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/FederatedComputeInput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/FederatedComputeInput;")