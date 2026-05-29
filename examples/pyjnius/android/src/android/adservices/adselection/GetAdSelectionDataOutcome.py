from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetAdSelectionDataOutcome"]

class GetAdSelectionDataOutcome(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/GetAdSelectionDataOutcome"
    getAdSelectionData = JavaMethod("()[B")
    getAdSelectionDataId = JavaMethod("()J")
    getAdSelectionId = JavaMethod("()J")