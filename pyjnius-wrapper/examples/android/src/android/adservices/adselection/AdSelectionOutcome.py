from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdSelectionOutcome"]

class AdSelectionOutcome(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AdSelectionOutcome"
    NO_OUTCOME = JavaStaticField("Landroid/adservices/adselection/AdSelectionOutcome;")
    getRenderUri = JavaMethod("()Landroid/net/Uri;")
    getAdSelectionId = JavaMethod("()J")
    hasOutcome = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/AdSelectionOutcome/Builder"
        __javaconstructor__ = [("()V", False)]
        setAdSelectionId = JavaMethod("(J)Landroid/adservices/adselection/AdSelectionOutcome$Builder;")
        setRenderUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/AdSelectionOutcome$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/AdSelectionOutcome;")