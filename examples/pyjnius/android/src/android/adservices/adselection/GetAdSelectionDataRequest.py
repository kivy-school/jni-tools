from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetAdSelectionDataRequest"]

class GetAdSelectionDataRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/GetAdSelectionDataRequest"
    getSeller = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getCoordinatorOriginUri = JavaMethod("()Landroid/net/Uri;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/GetAdSelectionDataRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        setSeller = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/GetAdSelectionDataRequest$Builder;")
        setCoordinatorOriginUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/GetAdSelectionDataRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/GetAdSelectionDataRequest;")