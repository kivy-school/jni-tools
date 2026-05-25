from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PdfRendererPreV"]

class PdfRendererPreV(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/PdfRendererPreV"
    __javaconstructor__ = [("(Landroid/os/ParcelFileDescriptor;)V", False), ("(Landroid/os/ParcelFileDescriptor;Landroid/graphics/pdf/LoadParams;)V", False)]
    DOCUMENT_LINEARIZED_TYPE_LINEARIZED = JavaStaticField("I")
    DOCUMENT_LINEARIZED_TYPE_NON_LINEARIZED = JavaStaticField("I")
    PDF_FORM_TYPE_ACRO_FORM = JavaStaticField("I")
    PDF_FORM_TYPE_NONE = JavaStaticField("I")
    PDF_FORM_TYPE_XFA_FOREGROUND = JavaStaticField("I")
    PDF_FORM_TYPE_XFA_FULL = JavaStaticField("I")
    getPageCount = JavaMethod("()I")
    getDocumentLinearizationType = JavaMethod("()I")
    openPage = JavaMethod("(I)Landroid/graphics/pdf/PdfRendererPreV$Page;")
    getPdfFormType = JavaMethod("()I")
    write = JavaMethod("(Landroid/os/ParcelFileDescriptor;Z)V")
    close = JavaMethod("()V")
    finalize = JavaMethod("()V")

    class Page(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/PdfRendererPreV/Page"
        getIndex = JavaMethod("()I")
        render = JavaMethod("(Landroid/graphics/Bitmap;Landroid/graphics/Rect;Landroid/graphics/Matrix;Landroid/graphics/pdf/RenderParams;)V")
        getTextContents = JavaMethod("()Ljava/util/List;")
        getImageContents = JavaMethod("()Ljava/util/List;")
        getWidth = JavaMethod("()I")
        getHeight = JavaMethod("()I")
        searchText = JavaMethod("(Ljava/lang/String;)Ljava/util/List;")
        selectContent = JavaMethod("(Landroid/graphics/pdf/models/selection/SelectionBoundary;Landroid/graphics/pdf/models/selection/SelectionBoundary;)Landroid/graphics/pdf/models/selection/PageSelection;")
        getLinkContents = JavaMethod("()Ljava/util/List;")
        getGotoLinks = JavaMethod("()Ljava/util/List;")
        getFormWidgetInfos = JavaMultipleMethod([("()Ljava/util/List;", False, False), ("([I)Ljava/util/List;", False, False)])
        getFormWidgetInfoAtIndex = JavaMethod("(I)Landroid/graphics/pdf/models/FormWidgetInfo;")
        getFormWidgetInfoAtPosition = JavaMethod("(II)Landroid/graphics/pdf/models/FormWidgetInfo;")
        applyEdit = JavaMethod("(Landroid/graphics/pdf/models/FormEditRecord;)Ljava/util/List;")
        close = JavaMethod("()V")
        finalize = JavaMethod("()V")