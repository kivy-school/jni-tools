from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InferenceInput"]

class InferenceInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/InferenceInput"
    getParams = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceInput$Params;")
    getInputData = JavaMethod("()[Ljava/lang/Object;")
    getBatchSize = JavaMethod("()I")
    getExpectedOutputStructure = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceOutput;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/InferenceInput/Builder"
        __javaconstructor__ = [("(Landroid/adservices/ondevicepersonalization/InferenceInput$Params;[Ljava/lang/Object;Landroid/adservices/ondevicepersonalization/InferenceOutput;)V", False)]
        setParams = JavaMethod("(Landroid/adservices/ondevicepersonalization/InferenceInput$Params;)Landroid/adservices/ondevicepersonalization/InferenceInput$Builder;")
        setInputData = JavaMethod("([Ljava/lang/Object;)Landroid/adservices/ondevicepersonalization/InferenceInput$Builder;", varargs=True)
        setBatchSize = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/InferenceInput$Builder;")
        setExpectedOutputStructure = JavaMethod("(Landroid/adservices/ondevicepersonalization/InferenceOutput;)Landroid/adservices/ondevicepersonalization/InferenceInput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceInput;")

    class Params(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/InferenceInput/Params"
        DELEGATE_CPU = JavaStaticField("I")
        MODEL_TYPE_TENSORFLOW_LITE = JavaStaticField("I")
        getKeyValueStore = JavaMethod("()Landroid/adservices/ondevicepersonalization/KeyValueStore;")
        getModelKey = JavaMethod("()Ljava/lang/String;")
        getDelegateType = JavaMethod("()I")
        getModelType = JavaMethod("()I")
        getRecommendedNumThreads = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/adservices/ondevicepersonalization/InferenceInput/Params/Builder"
            __javaconstructor__ = [("(Landroid/adservices/ondevicepersonalization/KeyValueStore;Ljava/lang/String;)V", False)]
            setKeyValueStore = JavaMethod("(Landroid/adservices/ondevicepersonalization/KeyValueStore;)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            setModelKey = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            setDelegateType = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            setModelType = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            setRecommendedNumThreads = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            build = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceInput$Params;")