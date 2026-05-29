from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdSelectionOutcome"]

class AdSelectionOutcome(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AdSelectionOutcome"
    NO_OUTCOME = JavaStaticField("Landroid/adservices/adselection/AdSelectionOutcome;")
    getComponentAdUris = JavaMethod("()Ljava/util/List;")
    getRenderUri = JavaMethod("()Landroid/net/Uri;")
    getWinningSeller = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    hasOutcome = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getAdSelectionId = JavaMethod("()J")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/AdSelectionOutcome$Builder"
        __javaconstructor__ = [("()V", False)]
        setRenderUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/AdSelectionOutcome$Builder;")
        setAdSelectionId = JavaMethod("(J)Landroid/adservices/adselection/AdSelectionOutcome$Builder;")
        setComponentAdUris = JavaMethod("(Ljava/util/List;)Landroid/adservices/adselection/AdSelectionOutcome$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/AdSelectionOutcome;")