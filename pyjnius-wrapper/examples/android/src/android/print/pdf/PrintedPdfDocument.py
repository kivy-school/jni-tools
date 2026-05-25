from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintedPdfDocument"]

class PrintedPdfDocument(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/pdf/PrintedPdfDocument"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/print/PrintAttributes;)V", False)]
    startPage = JavaMethod("(I)Landroid/graphics/pdf/PdfDocument$Page;")
    getPageWidth = JavaMethod("()I")
    getPageHeight = JavaMethod("()I")
    getPageContentRect = JavaMethod("()Landroid/graphics/Rect;")