from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InferenceOutput"]

class InferenceOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/InferenceOutput"
    getDataOutputs = JavaMethod("()Ljava/util/Map;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/InferenceOutput/Builder"
        __javaconstructor__ = [("()V", False)]
        setDataOutputs = JavaMethod("(Ljava/util/Map;)Landroid/adservices/ondevicepersonalization/InferenceOutput$Builder;")
        addDataOutput = JavaMethod("(ILjava/lang/Object;)Landroid/adservices/ondevicepersonalization/InferenceOutput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceOutput;")