from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AddAdSelectionOverrideRequest"]

class AddAdSelectionOverrideRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AddAdSelectionOverrideRequest"
    __javaconstructor__ = [("(Landroid/adservices/adselection/AdSelectionConfig;Ljava/lang/String;Landroid/adservices/common/AdSelectionSignals;Landroid/adservices/adselection/PerBuyerDecisionLogic;)V", False), ("(Landroid/adservices/adselection/AdSelectionConfig;Ljava/lang/String;Landroid/adservices/common/AdSelectionSignals;)V", False)]
    getDecisionLogicJs = JavaMethod("()Ljava/lang/String;")
    getPerBuyerDecisionLogic = JavaMethod("()Landroid/adservices/adselection/PerBuyerDecisionLogic;")
    getTrustedScoringSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getAdSelectionConfig = JavaMethod("()Landroid/adservices/adselection/AdSelectionConfig;")