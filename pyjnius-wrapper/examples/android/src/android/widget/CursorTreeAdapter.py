from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CursorTreeAdapter"]

class CursorTreeAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/CursorTreeAdapter"
    __javaconstructor__ = [("(Landroid/database/Cursor;Landroid/content/Context;)V", False), ("(Landroid/database/Cursor;Landroid/content/Context;Z)V", False)]
    getChildrenCursor = JavaMethod("(Landroid/database/Cursor;)Landroid/database/Cursor;")
    setGroupCursor = JavaMethod("(Landroid/database/Cursor;)V")
    setChildrenCursor = JavaMethod("(ILandroid/database/Cursor;)V")
    getChild = JavaMethod("(II)Landroid/database/Cursor;")
    getChildId = JavaMethod("(II)J")
    getChildrenCount = JavaMethod("(I)I")
    getGroup = JavaMethod("(I)Landroid/database/Cursor;")
    getGroupCount = JavaMethod("()I")
    getGroupId = JavaMethod("(I)J")
    getGroupView = JavaMethod("(IZLandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    newGroupView = JavaMethod("(Landroid/content/Context;Landroid/database/Cursor;ZLandroid/view/ViewGroup;)Landroid/view/View;")
    bindGroupView = JavaMethod("(Landroid/view/View;Landroid/content/Context;Landroid/database/Cursor;Z)V")
    getChildView = JavaMethod("(IIZLandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    newChildView = JavaMethod("(Landroid/content/Context;Landroid/database/Cursor;ZLandroid/view/ViewGroup;)Landroid/view/View;")
    bindChildView = JavaMethod("(Landroid/view/View;Landroid/content/Context;Landroid/database/Cursor;Z)V")
    isChildSelectable = JavaMethod("(II)Z")
    hasStableIds = JavaMethod("()Z")
    notifyDataSetChanged = JavaMultipleMethod([("()V", False, False), ("(Z)V", False, False)])
    notifyDataSetInvalidated = JavaMethod("()V")
    onGroupCollapsed = JavaMethod("(I)V")
    convertToString = JavaMethod("(Landroid/database/Cursor;)Ljava/lang/String;")
    runQueryOnBackgroundThread = JavaMethod("(Ljava/lang/CharSequence;)Landroid/database/Cursor;")
    getFilter = JavaMethod("()Landroid/widget/Filter;")
    getFilterQueryProvider = JavaMethod("()Landroid/widget/FilterQueryProvider;")
    setFilterQueryProvider = JavaMethod("(Landroid/widget/FilterQueryProvider;)V")
    changeCursor = JavaMethod("(Landroid/database/Cursor;)V")
    getCursor = JavaMethod("()Landroid/database/Cursor;")