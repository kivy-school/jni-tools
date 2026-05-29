from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExpandableListAdapter"]

class ExpandableListAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ExpandableListAdapter"
    isEmpty = JavaMethod("()Z")
    getGroup = JavaMethod("(I)Ljava/lang/Object;")
    getChildId = JavaMethod("(II)J")
    getChildView = JavaMethod("(IIZLandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getChildrenCount = JavaMethod("(I)I")
    getGroupCount = JavaMethod("()I")
    getGroupId = JavaMethod("(I)J")
    getGroupView = JavaMethod("(IZLandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    isChildSelectable = JavaMethod("(II)Z")
    onGroupCollapsed = JavaMethod("(I)V")
    getChild = JavaMethod("(II)Ljava/lang/Object;")
    areAllItemsEnabled = JavaMethod("()Z")
    hasStableIds = JavaMethod("()Z")
    registerDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    unregisterDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    getCombinedChildId = JavaMethod("(JJ)J")
    getCombinedGroupId = JavaMethod("(J)J")
    onGroupExpanded = JavaMethod("(I)V")