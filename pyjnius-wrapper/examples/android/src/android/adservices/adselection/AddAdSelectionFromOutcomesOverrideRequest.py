from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AddAdSelectionFromOutcomesOverrideRequest"]

class AddAdSelectionFromOutcomesOverrideRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AddAdSelectionFromOutcomesOverrideRequest"
    __javaconstructor__ = [("(Landroid/adservices/adselection/AdSelectionFromOutcomesConfig;Ljava/lang/String;Landroid/adservices/common/AdSelectionSignals;)V", False)]
    getAdSelectionFromOutcomesConfig = JavaMethod("()Landroid/adservices/adselection/AdSelectionFromOutcomesConfig;")
    getOutcomeSelectionLogicJs = JavaMethod("()Ljava/lang/String;")
    getOutcomeSelectionTrustedSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")