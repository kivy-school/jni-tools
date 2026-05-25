from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Selection"]

class Selection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/Selection"
    SELECTION_END = JavaStaticField("Ljava/lang/Object;")
    SELECTION_START = JavaStaticField("Ljava/lang/Object;")
    getSelectionStart = JavaStaticMethod("(Ljava/lang/CharSequence;)I")
    getSelectionEnd = JavaStaticMethod("(Ljava/lang/CharSequence;)I")
    setSelection = JavaMultipleMethod([("(Landroid/text/Spannable;II)V", True, False), ("(Landroid/text/Spannable;I)V", True, False)])
    selectAll = JavaStaticMethod("(Landroid/text/Spannable;)V")
    extendSelection = JavaStaticMethod("(Landroid/text/Spannable;I)V")
    removeSelection = JavaStaticMethod("(Landroid/text/Spannable;)V")
    moveUp = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveDown = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveLeft = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveRight = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveToParagraphStart = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveToParagraphEnd = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    extendToParagraphStart = JavaStaticMethod("(Landroid/text/Spannable;)Z")
    extendToParagraphEnd = JavaStaticMethod("(Landroid/text/Spannable;)Z")
    extendUp = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    extendDown = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    extendLeft = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    extendRight = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    extendToLeftEdge = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    extendToRightEdge = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveToLeftEdge = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")
    moveToRightEdge = JavaStaticMethod("(Landroid/text/Spannable;Landroid/text/Layout;)Z")