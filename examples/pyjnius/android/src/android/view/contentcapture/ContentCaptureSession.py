from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentCaptureSession"]

class ContentCaptureSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/ContentCaptureSession"
    newViewStructure = JavaMethod("(Landroid/view/View;)Landroid/view/ViewStructure;")
    notifyViewAppeared = JavaMethod("(Landroid/view/ViewStructure;)V")
    newAutofillId = JavaMethod("(Landroid/view/autofill/AutofillId;J)Landroid/view/autofill/AutofillId;")
    createContentCaptureSession = JavaMethod("(Landroid/view/contentcapture/ContentCaptureContext;)Landroid/view/contentcapture/ContentCaptureSession;")
    getContentCaptureContext = JavaMethod("()Landroid/view/contentcapture/ContentCaptureContext;")
    getContentCaptureSessionId = JavaMethod("()Landroid/view/contentcapture/ContentCaptureSessionId;")
    newVirtualViewStructure = JavaMethod("(Landroid/view/autofill/AutofillId;J)Landroid/view/ViewStructure;")
    notifySessionPaused = JavaMethod("()V")
    notifySessionResumed = JavaMethod("()V")
    notifyViewDisappeared = JavaMethod("(Landroid/view/autofill/AutofillId;)V")
    notifyViewInsetsChanged = JavaMethod("(Landroid/graphics/Insets;)V")
    notifyViewTextChanged = JavaMethod("(Landroid/view/autofill/AutofillId;Ljava/lang/CharSequence;)V")
    notifyViewsAppeared = JavaMethod("(Ljava/util/List;)V")
    notifyViewsDisappeared = JavaMethod("(Landroid/view/autofill/AutofillId;[J)V")
    setContentCaptureContext = JavaMethod("(Landroid/view/contentcapture/ContentCaptureContext;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    destroy = JavaMethod("()V")