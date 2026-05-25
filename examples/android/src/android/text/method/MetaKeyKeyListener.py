from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MetaKeyKeyListener"]

class MetaKeyKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/MetaKeyKeyListener"
    __javaconstructor__ = [("()V", False)]
    META_ALT_LOCKED = JavaStaticField("I")
    META_ALT_ON = JavaStaticField("I")
    META_CAP_LOCKED = JavaStaticField("I")
    META_SHIFT_ON = JavaStaticField("I")
    META_SYM_LOCKED = JavaStaticField("I")
    META_SYM_ON = JavaStaticField("I")
    resetMetaState = JavaStaticMethod("(Landroid/text/Spannable;)V")
    getMetaState = JavaMultipleMethod([("(Ljava/lang/CharSequence;)I", True, False), ("(Ljava/lang/CharSequence;Landroid/view/KeyEvent;)I", True, False), ("(Ljava/lang/CharSequence;I)I", True, False), ("(Ljava/lang/CharSequence;ILandroid/view/KeyEvent;)I", True, False), ("(J)I", True, False), ("(JI)I", True, False)])
    adjustMetaAfterKeypress = JavaMultipleMethod([("(Landroid/text/Spannable;)V", True, False), ("(J)J", True, False)])
    isMetaTracker = JavaStaticMethod("(Ljava/lang/CharSequence;Ljava/lang/Object;)Z")
    isSelectingMetaTracker = JavaStaticMethod("(Ljava/lang/CharSequence;Ljava/lang/Object;)Z")
    resetLockedMeta = JavaMultipleMethod([("(Landroid/text/Spannable;)V", True, False), ("(J)J", True, False)])
    onKeyDown = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    onKeyUp = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    clearMetaKeyState = JavaMultipleMethod([("(Landroid/view/View;Landroid/text/Editable;I)V", False, False), ("(Landroid/text/Editable;I)V", True, False), ("(JI)J", False, False)])
    handleKeyDown = JavaStaticMethod("(JILandroid/view/KeyEvent;)J")
    handleKeyUp = JavaStaticMethod("(JILandroid/view/KeyEvent;)J")