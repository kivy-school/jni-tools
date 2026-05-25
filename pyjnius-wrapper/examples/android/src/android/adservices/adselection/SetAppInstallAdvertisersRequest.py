from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SetAppInstallAdvertisersRequest"]

class SetAppInstallAdvertisersRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/SetAppInstallAdvertisersRequest"
    getAdvertisers = JavaMethod("()Ljava/util/Set;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/SetAppInstallAdvertisersRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        setAdvertisers = JavaMethod("(Ljava/util/Set;)Landroid/adservices/adselection/SetAppInstallAdvertisersRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/SetAppInstallAdvertisersRequest;")