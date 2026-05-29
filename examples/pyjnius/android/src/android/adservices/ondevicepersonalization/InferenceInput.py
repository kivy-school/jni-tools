from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InferenceInput"]

class InferenceInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/InferenceInput"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getBatchSize = JavaMethod("()I")
    getExpectedOutputStructure = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceOutput;")
    getInputData = JavaMethod("()[Ljava/lang/Object;")
    getParams = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceInput$Params;")

    class Params(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/InferenceInput$Params"
        DELEGATE_CPU = JavaStaticField("I")
        MODEL_TYPE_TENSORFLOW_LITE = JavaStaticField("I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getModelType = JavaMethod("()I")
        getKeyValueStore = JavaMethod("()Landroid/adservices/ondevicepersonalization/KeyValueStore;")
        getDelegateType = JavaMethod("()I")
        getRecommendedNumThreads = JavaMethod("()I")
        getModelKey = JavaMethod("()Ljava/lang/String;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/adservices/ondevicepersonalization/InferenceInput$Params$Builder"
            __javaconstructor__ = [("(Landroid/adservices/ondevicepersonalization/KeyValueStore;Ljava/lang/String;)V", False)]
            build = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceInput$Params;")
            setDelegateType = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            setModelType = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            setModelKey = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            setKeyValueStore = JavaMethod("(Landroid/adservices/ondevicepersonalization/KeyValueStore;)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            setRecommendedNumThreads = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/InferenceInput$Builder"
        __javaconstructor__ = [("(Landroid/adservices/ondevicepersonalization/InferenceInput$Params;[Ljava/lang/Object;Landroid/adservices/ondevicepersonalization/InferenceOutput;)V", False)]
        setParams = JavaMethod("(Landroid/adservices/ondevicepersonalization/InferenceInput$Params;)Landroid/adservices/ondevicepersonalization/InferenceInput$Builder;")
        setBatchSize = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/InferenceInput$Builder;")
        setExpectedOutputStructure = JavaMethod("(Landroid/adservices/ondevicepersonalization/InferenceOutput;)Landroid/adservices/ondevicepersonalization/InferenceInput$Builder;")
        setInputData = JavaMethod("([Ljava/lang/Object;)Landroid/adservices/ondevicepersonalization/InferenceInput$Builder;", varargs=True)
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceInput;")