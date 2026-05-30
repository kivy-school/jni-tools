from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LoadParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/LoadParams"
    getPassword = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/LoadParams$Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/graphics/pdf/LoadParams;")
        setPassword = JavaMethod("(Ljava/lang/String;)Landroid/graphics/pdf/LoadParams$Builder;")

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
    getPdfFormType = JavaMethod("()I")
    getDocumentLinearizationType = JavaMethod("()I")
    openPage = JavaMethod("(I)Landroid/graphics/pdf/PdfRendererPreV$Page;")
    write = JavaMethod("(Landroid/os/ParcelFileDescriptor;Z)V")
    close = JavaMethod("()V")

    class Page(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/PdfRendererPreV$Page"
        searchText = JavaMethod("(Ljava/lang/String;)Ljava/util/List;")
        render = JavaMethod("(Landroid/graphics/Bitmap;Landroid/graphics/Rect;Landroid/graphics/Matrix;Landroid/graphics/pdf/RenderParams;)V")
        applyEdit = JavaMethod("(Landroid/graphics/pdf/models/FormEditRecord;)Ljava/util/List;")
        getFormWidgetInfos = JavaMultipleMethod([("([I)Ljava/util/List;", False, False), ("()Ljava/util/List;", False, False)])
        getFormWidgetInfoAtIndex = JavaMethod("(I)Landroid/graphics/pdf/models/FormWidgetInfo;")
        getFormWidgetInfoAtPosition = JavaMethod("(II)Landroid/graphics/pdf/models/FormWidgetInfo;")
        getGotoLinks = JavaMethod("()Ljava/util/List;")
        getImageContents = JavaMethod("()Ljava/util/List;")
        getLinkContents = JavaMethod("()Ljava/util/List;")
        getTextContents = JavaMethod("()Ljava/util/List;")
        selectContent = JavaMethod("(Landroid/graphics/pdf/models/selection/SelectionBoundary;Landroid/graphics/pdf/models/selection/SelectionBoundary;)Landroid/graphics/pdf/models/selection/PageSelection;")
        close = JavaMethod("()V")
        getIndex = JavaMethod("()I")
        getHeight = JavaMethod("()I")
        getWidth = JavaMethod("()I")

class RenderParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/RenderParams"
    FLAG_RENDER_HIGHLIGHT_ANNOTATIONS = JavaStaticField("I")
    FLAG_RENDER_TEXT_ANNOTATIONS = JavaStaticField("I")
    RENDER_MODE_FOR_DISPLAY = JavaStaticField("I")
    RENDER_MODE_FOR_PRINT = JavaStaticField("I")
    getRenderFlags = JavaMethod("()I")
    getRenderMode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/RenderParams$Builder"
        __javaconstructor__ = [("(I)V", False)]
        setRenderFlags = JavaMultipleMethod([("(II)Landroid/graphics/pdf/RenderParams$Builder;", False, False), ("(I)Landroid/graphics/pdf/RenderParams$Builder;", False, False)])
        build = JavaMethod("()Landroid/graphics/pdf/RenderParams;")

class PdfDocument(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/PdfDocument"
    __javaconstructor__ = [("()V", False)]
    finishPage = JavaMethod("(Landroid/graphics/pdf/PdfDocument$Page;)V")
    getPages = JavaMethod("()Ljava/util/List;")
    startPage = JavaMethod("(Landroid/graphics/pdf/PdfDocument$PageInfo;)Landroid/graphics/pdf/PdfDocument$Page;")
    close = JavaMethod("()V")
    writeTo = JavaMethod("(Ljava/io/OutputStream;)V")

    class PageInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/PdfDocument$PageInfo"
        getPageNumber = JavaMethod("()I")
        getContentRect = JavaMethod("()Landroid/graphics/Rect;")
        getPageHeight = JavaMethod("()I")
        getPageWidth = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/graphics/pdf/PdfDocument$PageInfo$Builder"
            __javaconstructor__ = [("(III)V", False)]
            setContentRect = JavaMethod("(Landroid/graphics/Rect;)Landroid/graphics/pdf/PdfDocument$PageInfo$Builder;")
            create = JavaMethod("()Landroid/graphics/pdf/PdfDocument$PageInfo;")

    class Page(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/PdfDocument$Page"
        getInfo = JavaMethod("()Landroid/graphics/pdf/PdfDocument$PageInfo;")
        getCanvas = JavaMethod("()Landroid/graphics/Canvas;")

class PdfRenderer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/PdfRenderer"
    __javaconstructor__ = [("(Landroid/os/ParcelFileDescriptor;)V", False), ("(Landroid/os/ParcelFileDescriptor;Landroid/graphics/pdf/LoadParams;)V", False)]
    DOCUMENT_LINEARIZED_TYPE_LINEARIZED = JavaStaticField("I")
    DOCUMENT_LINEARIZED_TYPE_NON_LINEARIZED = JavaStaticField("I")
    PDF_FORM_TYPE_ACRO_FORM = JavaStaticField("I")
    PDF_FORM_TYPE_NONE = JavaStaticField("I")
    PDF_FORM_TYPE_XFA_FOREGROUND = JavaStaticField("I")
    PDF_FORM_TYPE_XFA_FULL = JavaStaticField("I")
    getPageCount = JavaMethod("()I")
    getPdfFormType = JavaMethod("()I")
    getDocumentLinearizationType = JavaMethod("()I")
    openPage = JavaMethod("(I)Landroid/graphics/pdf/PdfRenderer$Page;")
    shouldScaleForPrinting = JavaMethod("()Z")
    write = JavaMethod("(Landroid/os/ParcelFileDescriptor;Z)V")
    close = JavaMethod("()V")

    class Page(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/PdfRenderer$Page"
        RENDER_MODE_FOR_DISPLAY = JavaStaticField("I")
        RENDER_MODE_FOR_PRINT = JavaStaticField("I")
        searchText = JavaMethod("(Ljava/lang/String;)Ljava/util/List;")
        render = JavaMultipleMethod([("(Landroid/graphics/Bitmap;Landroid/graphics/Rect;Landroid/graphics/Matrix;I)V", False, False), ("(Landroid/graphics/Bitmap;Landroid/graphics/Rect;Landroid/graphics/Matrix;Landroid/graphics/pdf/RenderParams;)V", False, False)])
        applyEdit = JavaMethod("(Landroid/graphics/pdf/models/FormEditRecord;)Ljava/util/List;")
        getFormWidgetInfos = JavaMultipleMethod([("()Ljava/util/List;", False, False), ("([I)Ljava/util/List;", False, False)])
        getFormWidgetInfoAtIndex = JavaMethod("(I)Landroid/graphics/pdf/models/FormWidgetInfo;")
        getFormWidgetInfoAtPosition = JavaMethod("(II)Landroid/graphics/pdf/models/FormWidgetInfo;")
        getGotoLinks = JavaMethod("()Ljava/util/List;")
        getImageContents = JavaMethod("()Ljava/util/List;")
        getLinkContents = JavaMethod("()Ljava/util/List;")
        getTextContents = JavaMethod("()Ljava/util/List;")
        selectContent = JavaMethod("(Landroid/graphics/pdf/models/selection/SelectionBoundary;Landroid/graphics/pdf/models/selection/SelectionBoundary;)Landroid/graphics/pdf/models/selection/PageSelection;")
        close = JavaMethod("()V")
        getIndex = JavaMethod("()I")
        getHeight = JavaMethod("()I")
        getWidth = JavaMethod("()I")