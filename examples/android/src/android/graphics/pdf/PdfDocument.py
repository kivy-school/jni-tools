from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PdfDocument"]

class PdfDocument(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/PdfDocument"
    __javaconstructor__ = [("()V", False)]
    startPage = JavaMethod("(Landroid/graphics/pdf/PdfDocument$PageInfo;)Landroid/graphics/pdf/PdfDocument$Page;")
    finishPage = JavaMethod("(Landroid/graphics/pdf/PdfDocument$Page;)V")
    writeTo = JavaMethod("(Ljava/io/OutputStream;)V")
    getPages = JavaMethod("()Ljava/util/List;")
    close = JavaMethod("()V")
    finalize = JavaMethod("()V")

    class Page(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/PdfDocument/Page"
        getCanvas = JavaMethod("()Landroid/graphics/Canvas;")
        getInfo = JavaMethod("()Landroid/graphics/pdf/PdfDocument$PageInfo;")

    class PageInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/PdfDocument/PageInfo"
        getPageWidth = JavaMethod("()I")
        getPageHeight = JavaMethod("()I")
        getContentRect = JavaMethod("()Landroid/graphics/Rect;")
        getPageNumber = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/graphics/pdf/PdfDocument/PageInfo/Builder"
            __javaconstructor__ = [("(III)V", False)]
            setContentRect = JavaMethod("(Landroid/graphics/Rect;)Landroid/graphics/pdf/PdfDocument$PageInfo$Builder;")
            create = JavaMethod("()Landroid/graphics/pdf/PdfDocument$PageInfo;")