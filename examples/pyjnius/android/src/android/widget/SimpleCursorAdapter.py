from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimpleCursorAdapter"]

class SimpleCursorAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/SimpleCursorAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;ILandroid/database/Cursor;[Ljava/lang/String;[I)V", False), ("(Landroid/content/Context;ILandroid/database/Cursor;[Ljava/lang/String;[II)V", False)]
    bindView = JavaMethod("(Landroid/view/View;Landroid/content/Context;Landroid/database/Cursor;)V")
    getViewBinder = JavaMethod("()Landroid/widget/SimpleCursorAdapter$ViewBinder;")
    setViewBinder = JavaMethod("(Landroid/widget/SimpleCursorAdapter$ViewBinder;)V")
    setViewImage = JavaMethod("(Landroid/widget/ImageView;Ljava/lang/String;)V")
    setViewText = JavaMethod("(Landroid/widget/TextView;Ljava/lang/String;)V")
    getStringConversionColumn = JavaMethod("()I")
    setStringConversionColumn = JavaMethod("(I)V")
    getCursorToStringConverter = JavaMethod("()Landroid/widget/SimpleCursorAdapter$CursorToStringConverter;")
    setCursorToStringConverter = JavaMethod("(Landroid/widget/SimpleCursorAdapter$CursorToStringConverter;)V")
    convertToString = JavaMethod("(Landroid/database/Cursor;)Ljava/lang/CharSequence;")
    swapCursor = JavaMethod("(Landroid/database/Cursor;)Landroid/database/Cursor;")
    changeCursorAndColumns = JavaMethod("(Landroid/database/Cursor;[Ljava/lang/String;[I)V")

    class CursorToStringConverter(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SimpleCursorAdapter/CursorToStringConverter"
        convertToString = JavaMethod("(Landroid/database/Cursor;)Ljava/lang/CharSequence;")

    class ViewBinder(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SimpleCursorAdapter/ViewBinder"
        setViewValue = JavaMethod("(Landroid/view/View;Landroid/database/Cursor;I)Z")