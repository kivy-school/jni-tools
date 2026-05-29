from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Selection"]

class Selection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/Selection"
    SELECTION_END = JavaStaticField("Ljava/lang/Object;")
    SELECTION_START = JavaStaticField("Ljava/lang/Object;")
    extendRight = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    extendLeft = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    extendDown = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    extendToLeftEdge = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    extendToParagraphEnd = JavaStaticMethod("(Landroid/text/Spannable;)Z")
    extendToParagraphStart = JavaStaticMethod("(Landroid/text/Spannable;)Z")
    extendToRightEdge = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    extendUp = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveDown = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveLeft = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveRight = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveToLeftEdge = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveToParagraphEnd = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveToParagraphStart = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveToRightEdge = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveUp = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    removeSelection = JavaStaticMethod("(Landroid/text/Spannable;)V")
    setSelection = JavaMultipleMethod([("(Landroid/text/Spannable;II)V", True, False), ("(Landroid/text/Spannable;I)V", True, False)])
    getSelectionEnd = JavaStaticMethod("(Ljava/lang/CharSequence;)I")
    getSelectionStart = JavaStaticMethod("(Ljava/lang/CharSequence;)I")
    extendSelection = JavaStaticMethod("(Landroid/text/Spannable;I)V")
    selectAll = JavaStaticMethod("(Landroid/text/Spannable;)V")