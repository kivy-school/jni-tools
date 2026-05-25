from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClipboardManager"]

class ClipboardManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ClipboardManager"
    setPrimaryClip = JavaMethod("(Landroid/content/ClipData;)V")
    clearPrimaryClip = JavaMethod("()V")
    getPrimaryClip = JavaMethod("()Landroid/content/ClipData;")
    getPrimaryClipDescription = JavaMethod("()Landroid/content/ClipDescription;")
    hasPrimaryClip = JavaMethod("()Z")
    addPrimaryClipChangedListener = JavaMethod("(Landroid/content/ClipboardManager$OnPrimaryClipChangedListener;)V")
    removePrimaryClipChangedListener = JavaMethod("(Landroid/content/ClipboardManager$OnPrimaryClipChangedListener;)V")
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    setText = JavaMethod("(Ljava/lang/CharSequence;)V")
    hasText = JavaMethod("()Z")

    class OnPrimaryClipChangedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/ClipboardManager/OnPrimaryClipChangedListener"
        onPrimaryClipChanged = JavaMethod("()V")