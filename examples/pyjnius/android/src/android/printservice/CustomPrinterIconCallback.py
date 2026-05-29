from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CustomPrinterIconCallback"]

class CustomPrinterIconCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/printservice/CustomPrinterIconCallback"
    onCustomPrinterIconLoaded = JavaMethod("(Landroid/graphics/drawable/Icon;)Z")