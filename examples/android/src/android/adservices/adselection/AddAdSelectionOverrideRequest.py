from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AddAdSelectionOverrideRequest"]

class AddAdSelectionOverrideRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AddAdSelectionOverrideRequest"
    __javaconstructor__ = [("(Landroid/adservices/adselection/AdSelectionConfig;Ljava/lang/String;Landroid/adservices/common/AdSelectionSignals;Landroid/adservices/adselection/PerBuyerDecisionLogic;)V", False), ("(Landroid/adservices/adselection/AdSelectionConfig;Ljava/lang/String;Landroid/adservices/common/AdSelectionSignals;)V", False)]
    getAdSelectionConfig = JavaMethod("()Landroid/adservices/adselection/AdSelectionConfig;")
    getDecisionLogicJs = JavaMethod("()Ljava/lang/String;")
    getTrustedScoringSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getPerBuyerDecisionLogic = JavaMethod("()Landroid/adservices/adselection/PerBuyerDecisionLogic;")