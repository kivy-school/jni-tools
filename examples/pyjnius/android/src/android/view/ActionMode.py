from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ActionMode"]

class ActionMode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ActionMode"
    __javaconstructor__ = [("()V", False)]
    DEFAULT_HIDE_DURATION = JavaStaticField("I")
    TYPE_FLOATING = JavaStaticField("I")
    TYPE_PRIMARY = JavaStaticField("I")
    getType = JavaMethod("()I")
    finish = JavaMethod("()V")
    getTag = JavaMethod("()Ljava/lang/Object;")
    onWindowFocusChanged = JavaMethod("(Z)V")
    setTag = JavaMethod("(Ljava/lang/Object;)V")
    hide = JavaMethod("(J)V")
    getMenu = JavaMethod("()Landroid/view/Menu;")
    getSubtitle = JavaMethod("()Ljava/lang/CharSequence;")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    setSubtitle = JavaMultipleMethod([("(I)V", False, False), ("(Ljava/lang/CharSequence;)V", False, False)])
    setTitle = JavaMultipleMethod([("(I)V", False, False), ("(Ljava/lang/CharSequence;)V", False, False)])
    getCustomView = JavaMethod("()Landroid/view/View;")
    getTitleOptionalHint = JavaMethod("()Z")
    invalidateContentRect = JavaMethod("()V")
    setCustomView = JavaMethod("(Landroid/view/View;)V")
    setTitleOptionalHint = JavaMethod("(Z)V")
    isTitleOptional = JavaMethod("()Z")
    setType = JavaMethod("(I)V")
    invalidate = JavaMethod("()V")
    getMenuInflater = JavaMethod("()Landroid/view/MenuInflater;")

    class Callback2(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ActionMode$Callback2"
        __javaconstructor__ = [("()V", False)]
        onGetContentRect = JavaMethod("(Landroid/view/ActionMode;Landroid/view/View;Landroid/graphics/Rect;)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ActionMode$Callback"
        onCreateActionMode = JavaMethod("(Landroid/view/ActionMode;Landroid/view/Menu;)Z")
        onActionItemClicked = JavaMethod("(Landroid/view/ActionMode;Landroid/view/MenuItem;)Z")
        onDestroyActionMode = JavaMethod("(Landroid/view/ActionMode;)V")
        onPrepareActionMode = JavaMethod("(Landroid/view/ActionMode;Landroid/view/Menu;)Z")