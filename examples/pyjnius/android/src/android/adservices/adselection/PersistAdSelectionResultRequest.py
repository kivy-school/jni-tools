from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PersistAdSelectionResultRequest"]

class PersistAdSelectionResultRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/PersistAdSelectionResultRequest"
    getSeller = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getAdSelectionResult = JavaMethod("()[B")
    getAdSelectionDataId = JavaMethod("()J")
    getAdSelectionId = JavaMethod("()J")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/PersistAdSelectionResultRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setAdSelectionId = JavaMethod("(J)Landroid/adservices/adselection/PersistAdSelectionResultRequest$Builder;")
        setAdSelectionResult = JavaMethod("([B)Landroid/adservices/adselection/PersistAdSelectionResultRequest$Builder;")
        setAdSelectionDataId = JavaMethod("(J)Landroid/adservices/adselection/PersistAdSelectionResultRequest$Builder;")
        setSeller = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/PersistAdSelectionResultRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/PersistAdSelectionResultRequest;")