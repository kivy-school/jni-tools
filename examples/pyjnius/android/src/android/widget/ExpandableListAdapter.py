from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExpandableListAdapter"]

class ExpandableListAdapter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ExpandableListAdapter"
    registerDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    unregisterDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    getGroupCount = JavaMethod("()I")
    getChildrenCount = JavaMethod("(I)I")
    getGroup = JavaMethod("(I)Ljava/lang/Object;")
    getChild = JavaMethod("(II)Ljava/lang/Object;")
    getGroupId = JavaMethod("(I)J")
    getChildId = JavaMethod("(II)J")
    hasStableIds = JavaMethod("()Z")
    getGroupView = JavaMethod("(IZLandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getChildView = JavaMethod("(IIZLandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    isChildSelectable = JavaMethod("(II)Z")
    areAllItemsEnabled = JavaMethod("()Z")
    isEmpty = JavaMethod("()Z")
    onGroupExpanded = JavaMethod("(I)V")
    onGroupCollapsed = JavaMethod("(I)V")
    getCombinedChildId = JavaMethod("(JJ)J")
    getCombinedGroupId = JavaMethod("(J)J")