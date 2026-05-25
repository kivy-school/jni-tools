from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentCaptureSession"]

class ContentCaptureSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/ContentCaptureSession"
    getContentCaptureSessionId = JavaMethod("()Landroid/view/contentcapture/ContentCaptureSessionId;")
    createContentCaptureSession = JavaMethod("(Landroid/view/contentcapture/ContentCaptureContext;)Landroid/view/contentcapture/ContentCaptureSession;")
    setContentCaptureContext = JavaMethod("(Landroid/view/contentcapture/ContentCaptureContext;)V")
    getContentCaptureContext = JavaMethod("()Landroid/view/contentcapture/ContentCaptureContext;")
    destroy = JavaMethod("()V")
    close = JavaMethod("()V")
    notifyViewAppeared = JavaMethod("(Landroid/view/ViewStructure;)V")
    notifyViewDisappeared = JavaMethod("(Landroid/view/autofill/AutofillId;)V")
    notifyViewsAppeared = JavaMethod("(Ljava/util/List;)V")
    notifyViewsDisappeared = JavaMethod("(Landroid/view/autofill/AutofillId;[J)V")
    notifyViewTextChanged = JavaMethod("(Landroid/view/autofill/AutofillId;Ljava/lang/CharSequence;)V")
    notifyViewInsetsChanged = JavaMethod("(Landroid/graphics/Insets;)V")
    notifySessionResumed = JavaMethod("()V")
    notifySessionPaused = JavaMethod("()V")
    newViewStructure = JavaMethod("(Landroid/view/View;)Landroid/view/ViewStructure;")
    newAutofillId = JavaMethod("(Landroid/view/autofill/AutofillId;J)Landroid/view/autofill/AutofillId;")
    newVirtualViewStructure = JavaMethod("(Landroid/view/autofill/AutofillId;J)Landroid/view/ViewStructure;")
    toString = JavaMethod("()Ljava/lang/String;")