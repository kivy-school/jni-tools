from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintedPdfDocument"]

class PrintedPdfDocument(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/pdf/PrintedPdfDocument"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/print/PrintAttributes;)V", False)]
    getPageWidth = JavaMethod("()I")
    getPageHeight = JavaMethod("()I")
    startPage = JavaMethod("(I)Landroid/graphics/pdf/PdfDocument$Page;")
    getPageContentRect = JavaMethod("()Landroid/graphics/Rect;")