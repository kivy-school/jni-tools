from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Html"]

class Html(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/Html"
    FROM_HTML_MODE_COMPACT = JavaStaticField("I")
    FROM_HTML_MODE_LEGACY = JavaStaticField("I")
    FROM_HTML_OPTION_USE_CSS_COLORS = JavaStaticField("I")
    FROM_HTML_SEPARATOR_LINE_BREAK_BLOCKQUOTE = JavaStaticField("I")
    FROM_HTML_SEPARATOR_LINE_BREAK_DIV = JavaStaticField("I")
    FROM_HTML_SEPARATOR_LINE_BREAK_HEADING = JavaStaticField("I")
    FROM_HTML_SEPARATOR_LINE_BREAK_LIST = JavaStaticField("I")
    FROM_HTML_SEPARATOR_LINE_BREAK_LIST_ITEM = JavaStaticField("I")
    FROM_HTML_SEPARATOR_LINE_BREAK_PARAGRAPH = JavaStaticField("I")
    TO_HTML_PARAGRAPH_LINES_CONSECUTIVE = JavaStaticField("I")
    TO_HTML_PARAGRAPH_LINES_INDIVIDUAL = JavaStaticField("I")
    toHtml = JavaMultipleMethod([("(Landroid/text/Spanned;I)Ljava/lang/String;", True, False), ("(Landroid/text/Spanned;)Ljava/lang/String;", True, False)])
    fromHtml = JavaMultipleMethod([("(Ljava/lang/String;I)Landroid/text/Spanned;", True, False), ("(Ljava/lang/String;ILandroid/text/Html$ImageGetter;Landroid/text/Html$TagHandler;)Landroid/text/Spanned;", True, False), ("(Ljava/lang/String;Landroid/text/Html$ImageGetter;Landroid/text/Html$TagHandler;)Landroid/text/Spanned;", True, False), ("(Ljava/lang/String;)Landroid/text/Spanned;", True, False)])
    escapeHtml = JavaStaticMethod("(Ljava/lang/CharSequence;)Ljava/lang/String;")

    class TagHandler(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/Html$TagHandler"
        handleTag = JavaMethod("(ZLjava/lang/String;Landroid/text/Editable;Lorg/xml/sax/XMLReader;)V")

    class ImageGetter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/Html$ImageGetter"
        getDrawable = JavaMethod("(Ljava/lang/String;)Landroid/graphics/drawable/Drawable;")