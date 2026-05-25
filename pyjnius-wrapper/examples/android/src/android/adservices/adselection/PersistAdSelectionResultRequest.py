from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PersistAdSelectionResultRequest"]

class PersistAdSelectionResultRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/PersistAdSelectionResultRequest"
    getAdSelectionId = JavaMethod("()J")
    getAdSelectionDataId = JavaMethod("()J")
    getSeller = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getAdSelectionResult = JavaMethod("()[B")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/PersistAdSelectionResultRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        setAdSelectionId = JavaMethod("(J)Landroid/adservices/adselection/PersistAdSelectionResultRequest$Builder;")
        setAdSelectionDataId = JavaMethod("(J)Landroid/adservices/adselection/PersistAdSelectionResultRequest$Builder;")
        setSeller = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/PersistAdSelectionResultRequest$Builder;")
        setAdSelectionResult = JavaMethod("([B)Landroid/adservices/adselection/PersistAdSelectionResultRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/PersistAdSelectionResultRequest;")