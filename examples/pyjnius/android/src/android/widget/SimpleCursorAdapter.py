from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimpleCursorAdapter"]

class SimpleCursorAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/SimpleCursorAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;ILandroid/database/Cursor;[Ljava/lang/String;[I)V", False), ("(Landroid/content/Context;ILandroid/database/Cursor;[Ljava/lang/String;[II)V", False)]
    FLAG_AUTO_REQUERY = JavaStaticField("I")
    FLAG_REGISTER_CONTENT_OBSERVER = JavaStaticField("I")
    IGNORE_ITEM_VIEW_TYPE = JavaStaticField("I")
    NO_SELECTION = JavaStaticField("I")
    convertToString = JavaMethod("(Landroid/database/Cursor;)Ljava/lang/CharSequence;")
    bindView = JavaMethod("(Landroid/view/View;Landroid/content/Context;Landroid/database/Cursor;)V")
    swapCursor = JavaMethod("(Landroid/database/Cursor;)Landroid/database/Cursor;")
    getViewBinder = JavaMethod("()Landroid/widget/SimpleCursorAdapter$ViewBinder;")
    setViewBinder = JavaMethod("(Landroid/widget/SimpleCursorAdapter$ViewBinder;)V")
    setViewImage = JavaMethod("(Landroid/widget/ImageView;Ljava/lang/String;)V")
    setViewText = JavaMethod("(Landroid/widget/TextView;Ljava/lang/String;)V")
    changeCursorAndColumns = JavaMethod("(Landroid/database/Cursor;[Ljava/lang/String;[I)V")
    getCursorToStringConverter = JavaMethod("()Landroid/widget/SimpleCursorAdapter$CursorToStringConverter;")
    getStringConversionColumn = JavaMethod("()I")
    setCursorToStringConverter = JavaMethod("(Landroid/widget/SimpleCursorAdapter$CursorToStringConverter;)V")
    setStringConversionColumn = JavaMethod("(I)V")

    class ViewBinder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SimpleCursorAdapter$ViewBinder"
        setViewValue = JavaMethod("(Landroid/view/View;Landroid/database/Cursor;I)Z")

    class CursorToStringConverter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SimpleCursorAdapter$CursorToStringConverter"
        convertToString = JavaMethod("(Landroid/database/Cursor;)Ljava/lang/CharSequence;")