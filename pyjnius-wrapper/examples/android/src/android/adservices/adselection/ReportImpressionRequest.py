from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReportImpressionRequest"]

class ReportImpressionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/ReportImpressionRequest"
    __javaconstructor__ = [("(JLandroid/adservices/adselection/AdSelectionConfig;)V", False), ("(J)V", False)]
    getAdSelectionId = JavaMethod("()J")
    getAdSelectionConfig = JavaMethod("()Landroid/adservices/adselection/AdSelectionConfig;")