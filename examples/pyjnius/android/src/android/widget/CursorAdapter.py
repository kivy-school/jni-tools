from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CursorAdapter"]

class CursorAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/CursorAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/database/Cursor;I)V", False), ("(Landroid/content/Context;Landroid/database/Cursor;Z)V", False), ("(Landroid/content/Context;Landroid/database/Cursor;)V", False)]
    FLAG_AUTO_REQUERY = JavaStaticField("I")
    FLAG_REGISTER_CONTENT_OBSERVER = JavaStaticField("I")
    IGNORE_ITEM_VIEW_TYPE = JavaStaticField("I")
    NO_SELECTION = JavaStaticField("I")
    getCount = JavaMethod("()I")
    changeCursor = JavaMethod("(Landroid/database/Cursor;)V")
    convertToString = JavaMethod("(Landroid/database/Cursor;)Ljava/lang/CharSequence;")
    getCursor = JavaMethod("()Landroid/database/Cursor;")
    getFilterQueryProvider = JavaMethod("()Landroid/widget/FilterQueryProvider;")
    runQueryOnBackgroundThread = JavaMethod("(Ljava/lang/CharSequence;)Landroid/database/Cursor;")
    setFilterQueryProvider = JavaMethod("(Landroid/widget/FilterQueryProvider;)V")
    getDropDownView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    bindView = JavaMethod("(Landroid/view/View;Landroid/content/Context;Landroid/database/Cursor;)V")
    swapCursor = JavaMethod("(Landroid/database/Cursor;)Landroid/database/Cursor;")
    newView = JavaMethod("(Landroid/content/Context;Landroid/database/Cursor;Landroid/view/ViewGroup;)Landroid/view/View;")
    newDropDownView = JavaMethod("(Landroid/content/Context;Landroid/database/Cursor;Landroid/view/ViewGroup;)Landroid/view/View;")
    getItem = JavaMethod("(I)Ljava/lang/Object;")
    getItemId = JavaMethod("(I)J")
    getView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    hasStableIds = JavaMethod("()Z")
    getDropDownViewTheme = JavaMethod("()Landroid/content/res/Resources$Theme;")
    getFilter = JavaMethod("()Landroid/widget/Filter;")
    setDropDownViewTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")