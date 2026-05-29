from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClipboardManager"]

class ClipboardManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ClipboardManager"
    hasText = JavaMethod("()Z")
    hasPrimaryClip = JavaMethod("()Z")
    clearPrimaryClip = JavaMethod("()V")
    getPrimaryClip = JavaMethod("()Landroid/content/ClipData;")
    setPrimaryClip = JavaMethod("(Landroid/content/ClipData;)V")
    addPrimaryClipChangedListener = JavaMethod("(Landroid/content/ClipboardManager$OnPrimaryClipChangedListener;)V")
    getPrimaryClipDescription = JavaMethod("()Landroid/content/ClipDescription;")
    removePrimaryClipChangedListener = JavaMethod("(Landroid/content/ClipboardManager$OnPrimaryClipChangedListener;)V")
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    setText = JavaMethod("(Ljava/lang/CharSequence;)V")

    class OnPrimaryClipChangedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/ClipboardManager$OnPrimaryClipChangedListener"
        onPrimaryClipChanged = JavaMethod("()V")