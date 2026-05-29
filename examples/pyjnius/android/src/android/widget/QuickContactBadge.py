from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QuickContactBadge"]

class QuickContactBadge(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/QuickContactBadge"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    mExcludeMimes = JavaField("[Ljava/lang/String;")
    onAttachedToWindow = JavaMethod("()V")
    drawableStateChanged = JavaMethod("()V")
    drawableHotspotChanged = JavaMethod("(FF)V")
    setMode = JavaMethod("(I)V")
    setPrioritizedMimeType = JavaMethod("(Ljava/lang/String;)V")
    onDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
    setImageToDefault = JavaMethod("()V")
    assignContactUri = JavaMethod("(Landroid/net/Uri;)V")
    assignContactFromEmail = JavaMultipleMethod([("(Ljava/lang/String;Z)V", False, False), ("(Ljava/lang/String;ZLandroid/os/Bundle;)V", False, False)])
    assignContactFromPhone = JavaMultipleMethod([("(Ljava/lang/String;Z)V", False, False), ("(Ljava/lang/String;ZLandroid/os/Bundle;)V", False, False)])
    setOverlay = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    onClick = JavaMethod("(Landroid/view/View;)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    setExcludeMimes = JavaMethod("([Ljava/lang/String;)V")