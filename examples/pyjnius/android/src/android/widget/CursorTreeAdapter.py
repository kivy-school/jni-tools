from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CursorTreeAdapter"]

class CursorTreeAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/CursorTreeAdapter"
    __javaconstructor__ = [("(Landroid/database/Cursor;Landroid/content/Context;)V", False), ("(Landroid/database/Cursor;Landroid/content/Context;Z)V", False)]
    getGroup = JavaMultipleMethod([("(I)Landroid/database/Cursor;", False, False), ("(I)Ljava/lang/Object;", False, False)])
    changeCursor = JavaMethod("(Landroid/database/Cursor;)V")
    convertToString = JavaMethod("(Landroid/database/Cursor;)Ljava/lang/String;")
    getChildId = JavaMethod("(II)J")
    getChildView = JavaMethod("(IIZLandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getChildrenCount = JavaMethod("(I)I")
    getCursor = JavaMethod("()Landroid/database/Cursor;")
    getFilterQueryProvider = JavaMethod("()Landroid/widget/FilterQueryProvider;")
    getGroupCount = JavaMethod("()I")
    getGroupId = JavaMethod("(I)J")
    getGroupView = JavaMethod("(IZLandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    isChildSelectable = JavaMethod("(II)Z")
    onGroupCollapsed = JavaMethod("(I)V")
    runQueryOnBackgroundThread = JavaMethod("(Ljava/lang/CharSequence;)Landroid/database/Cursor;")
    setChildrenCursor = JavaMethod("(ILandroid/database/Cursor;)V")
    setFilterQueryProvider = JavaMethod("(Landroid/widget/FilterQueryProvider;)V")
    setGroupCursor = JavaMethod("(Landroid/database/Cursor;)V")
    getChild = JavaMultipleMethod([("(II)Landroid/database/Cursor;", False, False), ("(II)Ljava/lang/Object;", False, False)])
    notifyDataSetChanged = JavaMultipleMethod([("()V", False, False), ("(Z)V", False, False)])
    notifyDataSetInvalidated = JavaMethod("()V")
    hasStableIds = JavaMethod("()Z")
    getFilter = JavaMethod("()Landroid/widget/Filter;")