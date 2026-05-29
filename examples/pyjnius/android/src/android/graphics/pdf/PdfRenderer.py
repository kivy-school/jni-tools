from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PdfRenderer"]

class PdfRenderer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/PdfRenderer"
    __javaconstructor__ = [("(Landroid/os/ParcelFileDescriptor;)V", False), ("(Landroid/os/ParcelFileDescriptor;Landroid/graphics/pdf/LoadParams;)V", False)]
    DOCUMENT_LINEARIZED_TYPE_LINEARIZED = JavaStaticField("I")
    DOCUMENT_LINEARIZED_TYPE_NON_LINEARIZED = JavaStaticField("I")
    PDF_FORM_TYPE_ACRO_FORM = JavaStaticField("I")
    PDF_FORM_TYPE_NONE = JavaStaticField("I")
    PDF_FORM_TYPE_XFA_FOREGROUND = JavaStaticField("I")
    PDF_FORM_TYPE_XFA_FULL = JavaStaticField("I")
    shouldScaleForPrinting = JavaMethod("()Z")
    openPage = JavaMethod("(I)Landroid/graphics/pdf/PdfRenderer$Page;")
    getPdfFormType = JavaMethod("()I")
    getPageCount = JavaMethod("()I")
    getDocumentLinearizationType = JavaMethod("()I")
    close = JavaMethod("()V")
    write = JavaMethod("(Landroid/os/ParcelFileDescriptor;Z)V")

    class Page(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/PdfRenderer$Page"
        RENDER_MODE_FOR_DISPLAY = JavaStaticField("I")
        RENDER_MODE_FOR_PRINT = JavaStaticField("I")
        searchText = JavaMethod("(Ljava/lang/String;)Ljava/util/List;")
        getImageContents = JavaMethod("()Ljava/util/List;")
        selectContent = JavaMethod("(Landroid/graphics/pdf/models/selection/SelectionBoundary;Landroid/graphics/pdf/models/selection/SelectionBoundary;)Landroid/graphics/pdf/models/selection/PageSelection;")
        getGotoLinks = JavaMethod("()Ljava/util/List;")
        getFormWidgetInfos = JavaMultipleMethod([("([I)Ljava/util/List;", False, False), ("()Ljava/util/List;", False, False)])
        getLinkContents = JavaMethod("()Ljava/util/List;")
        getFormWidgetInfoAtIndex = JavaMethod("(I)Landroid/graphics/pdf/models/FormWidgetInfo;")
        render = JavaMultipleMethod([("(Landroid/graphics/Bitmap;Landroid/graphics/Rect;Landroid/graphics/Matrix;Landroid/graphics/pdf/RenderParams;)V", False, False), ("(Landroid/graphics/Bitmap;Landroid/graphics/Rect;Landroid/graphics/Matrix;I)V", False, False)])
        getTextContents = JavaMethod("()Ljava/util/List;")
        applyEdit = JavaMethod("(Landroid/graphics/pdf/models/FormEditRecord;)Ljava/util/List;")
        getFormWidgetInfoAtPosition = JavaMethod("(II)Landroid/graphics/pdf/models/FormWidgetInfo;")
        close = JavaMethod("()V")
        getHeight = JavaMethod("()I")
        getWidth = JavaMethod("()I")
        getIndex = JavaMethod("()I")