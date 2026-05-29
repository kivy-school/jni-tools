from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoveAdSelectionFromOutcomesOverrideRequest"]

class RemoveAdSelectionFromOutcomesOverrideRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/RemoveAdSelectionFromOutcomesOverrideRequest"
    __javaconstructor__ = [("(Landroid/adservices/adselection/AdSelectionFromOutcomesConfig;)V", False)]
    getAdSelectionFromOutcomesConfig = JavaMethod("()Landroid/adservices/adselection/AdSelectionFromOutcomesConfig;")