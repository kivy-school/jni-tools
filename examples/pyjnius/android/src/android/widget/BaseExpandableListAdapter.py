from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseExpandableListAdapter"]

class BaseExpandableListAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/BaseExpandableListAdapter"
    __javaconstructor__ = [("()V", False)]
    isEmpty = JavaMethod("()Z")
    onGroupCollapsed = JavaMethod("(I)V")
    notifyDataSetChanged = JavaMethod("()V")
    notifyDataSetInvalidated = JavaMethod("()V")
    areAllItemsEnabled = JavaMethod("()Z")
    registerDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    unregisterDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    getChildTypeCount = JavaMethod("()I")
    getChildType = JavaMethod("(II)I")
    getCombinedChildId = JavaMethod("(JJ)J")
    getCombinedGroupId = JavaMethod("(J)J")
    getGroupType = JavaMethod("(I)I")
    getGroupTypeCount = JavaMethod("()I")
    onGroupExpanded = JavaMethod("(I)V")