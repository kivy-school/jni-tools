from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ActionMode"]

class ActionMode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ActionMode"
    __javaconstructor__ = [("()V", False)]
    DEFAULT_HIDE_DURATION = JavaStaticField("I")
    TYPE_FLOATING = JavaStaticField("I")
    TYPE_PRIMARY = JavaStaticField("I")
    setTag = JavaMethod("(Ljava/lang/Object;)V")
    getTag = JavaMethod("()Ljava/lang/Object;")
    setTitle = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    setSubtitle = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    setTitleOptionalHint = JavaMethod("(Z)V")
    getTitleOptionalHint = JavaMethod("()Z")
    isTitleOptional = JavaMethod("()Z")
    setCustomView = JavaMethod("(Landroid/view/View;)V")
    setType = JavaMethod("(I)V")
    getType = JavaMethod("()I")
    invalidate = JavaMethod("()V")
    invalidateContentRect = JavaMethod("()V")
    hide = JavaMethod("(J)V")
    finish = JavaMethod("()V")
    getMenu = JavaMethod("()Landroid/view/Menu;")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getSubtitle = JavaMethod("()Ljava/lang/CharSequence;")
    getCustomView = JavaMethod("()Landroid/view/View;")
    getMenuInflater = JavaMethod("()Landroid/view/MenuInflater;")
    onWindowFocusChanged = JavaMethod("(Z)V")

    class Callback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ActionMode/Callback"
        onCreateActionMode = JavaMethod("(Landroid/view/ActionMode;Landroid/view/Menu;)Z")
        onPrepareActionMode = JavaMethod("(Landroid/view/ActionMode;Landroid/view/Menu;)Z")
        onActionItemClicked = JavaMethod("(Landroid/view/ActionMode;Landroid/view/MenuItem;)Z")
        onDestroyActionMode = JavaMethod("(Landroid/view/ActionMode;)V")

    class Callback2(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ActionMode/Callback2"
        __javaconstructor__ = [("()V", False)]
        onGetContentRect = JavaMethod("(Landroid/view/ActionMode;Landroid/view/View;Landroid/graphics/Rect;)V")