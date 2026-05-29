from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExecuteInIsolatedServiceRequest"]

class ExecuteInIsolatedServiceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getService = JavaMethod("()Landroid/content/ComponentName;")
    getAppParams = JavaMethod("()Landroid/os/PersistableBundle;")
    getOutputSpec = JavaMethod("()Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$OutputSpec;")

    class OutputSpec(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$OutputSpec"
        DEFAULT = JavaStaticField("Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$OutputSpec;")
        OUTPUT_TYPE_BEST_VALUE = JavaStaticField("I")
        OUTPUT_TYPE_NULL = JavaStaticField("I")
        getMaxIntValue = JavaMethod("()I")
        buildBestValueSpec = JavaStaticMethod("(I)Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$OutputSpec;")
        getOutputType = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$Builder"
        __javaconstructor__ = [("(Landroid/content/ComponentName;)V", False)]
        setOutputSpec = JavaMethod("(Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$OutputSpec;)Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$Builder;")
        setAppParams = JavaMethod("(Landroid/os/PersistableBundle;)Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest;")