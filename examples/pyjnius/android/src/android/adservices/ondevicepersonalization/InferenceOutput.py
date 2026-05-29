from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InferenceOutput"]

class InferenceOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/InferenceOutput"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getDataOutputs = JavaMethod("()Ljava/util/Map;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/InferenceOutput$Builder"
        __javaconstructor__ = [("()V", False)]
        addDataOutput = JavaMethod("(ILjava/lang/Object;)Landroid/adservices/ondevicepersonalization/InferenceOutput$Builder;")
        setDataOutputs = JavaMethod("(Ljava/util/Map;)Landroid/adservices/ondevicepersonalization/InferenceOutput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceOutput;")