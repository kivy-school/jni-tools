from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReportImpressionRequest"]

class ReportImpressionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/ReportImpressionRequest"
    __javaconstructor__ = [("(J)V", False), ("(JLandroid/adservices/adselection/AdSelectionConfig;)V", False)]
    getAdSelectionConfig = JavaMethod("()Landroid/adservices/adselection/AdSelectionConfig;")
    getAdSelectionId = JavaMethod("()J")