from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CursorAdapter"]

class CursorAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/CursorAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/database/Cursor;)V", False), ("(Landroid/content/Context;Landroid/database/Cursor;Z)V", False), ("(Landroid/content/Context;Landroid/database/Cursor;I)V", False)]
    FLAG_AUTO_REQUERY = JavaStaticField("I")
    FLAG_REGISTER_CONTENT_OBSERVER = JavaStaticField("I")
    init = JavaMethod("(Landroid/content/Context;Landroid/database/Cursor;Z)V")
    setDropDownViewTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getDropDownViewTheme = JavaMethod("()Landroid/content/res/Resources$Theme;")
    getCursor = JavaMethod("()Landroid/database/Cursor;")
    getCount = JavaMethod("()I")
    getItem = JavaMethod("(I)Ljava/lang/Object;")
    getItemId = JavaMethod("(I)J")
    hasStableIds = JavaMethod("()Z")
    getView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getDropDownView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    newView = JavaMethod("(Landroid/content/Context;Landroid/database/Cursor;Landroid/view/ViewGroup;)Landroid/view/View;")
    newDropDownView = JavaMethod("(Landroid/content/Context;Landroid/database/Cursor;Landroid/view/ViewGroup;)Landroid/view/View;")
    bindView = JavaMethod("(Landroid/view/View;Landroid/content/Context;Landroid/database/Cursor;)V")
    changeCursor = JavaMethod("(Landroid/database/Cursor;)V")
    swapCursor = JavaMethod("(Landroid/database/Cursor;)Landroid/database/Cursor;")
    convertToString = JavaMethod("(Landroid/database/Cursor;)Ljava/lang/CharSequence;")
    runQueryOnBackgroundThread = JavaMethod("(Ljava/lang/CharSequence;)Landroid/database/Cursor;")
    getFilter = JavaMethod("()Landroid/widget/Filter;")
    getFilterQueryProvider = JavaMethod("()Landroid/widget/FilterQueryProvider;")
    setFilterQueryProvider = JavaMethod("(Landroid/widget/FilterQueryProvider;)V")
    onContentChanged = JavaMethod("()V")