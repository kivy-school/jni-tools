from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetAdSelectionDataOutcome"]

class GetAdSelectionDataOutcome(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/GetAdSelectionDataOutcome"
    getAdSelectionId = JavaMethod("()J")
    getAdSelectionDataId = JavaMethod("()J")
    getAdSelectionData = JavaMethod("()[B")