from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UpdateAdCounterHistogramRequest"]

class UpdateAdCounterHistogramRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/UpdateAdCounterHistogramRequest"
    getAdEventType = JavaMethod("()I")
    getCallerAdTech = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getAdSelectionId = JavaMethod("()J")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/UpdateAdCounterHistogramRequest$Builder"
        __javaconstructor__ = [("(JILandroid/adservices/common/AdTechIdentifier;)V", False)]
        setAdSelectionId = JavaMethod("(J)Landroid/adservices/adselection/UpdateAdCounterHistogramRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/UpdateAdCounterHistogramRequest;")
        setAdEventType = JavaMethod("(I)Landroid/adservices/adselection/UpdateAdCounterHistogramRequest$Builder;")
        setCallerAdTech = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/UpdateAdCounterHistogramRequest$Builder;")