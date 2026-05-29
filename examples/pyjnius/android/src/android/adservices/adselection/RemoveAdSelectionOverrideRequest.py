from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoveAdSelectionOverrideRequest"]

class RemoveAdSelectionOverrideRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/RemoveAdSelectionOverrideRequest"
    __javaconstructor__ = [("(Landroid/adservices/adselection/AdSelectionConfig;)V", False)]
    getAdSelectionConfig = JavaMethod("()Landroid/adservices/adselection/AdSelectionConfig;")