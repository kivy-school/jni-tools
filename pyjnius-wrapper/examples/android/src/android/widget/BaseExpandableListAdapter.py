from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseExpandableListAdapter"]

class BaseExpandableListAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/BaseExpandableListAdapter"
    __javaconstructor__ = [("()V", False)]
    registerDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    unregisterDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    notifyDataSetInvalidated = JavaMethod("()V")
    notifyDataSetChanged = JavaMethod("()V")
    areAllItemsEnabled = JavaMethod("()Z")
    onGroupCollapsed = JavaMethod("(I)V")
    onGroupExpanded = JavaMethod("(I)V")
    getCombinedChildId = JavaMethod("(JJ)J")
    getCombinedGroupId = JavaMethod("(J)J")
    isEmpty = JavaMethod("()Z")
    getChildType = JavaMethod("(II)I")
    getChildTypeCount = JavaMethod("()I")
    getGroupType = JavaMethod("(I)I")
    getGroupTypeCount = JavaMethod("()I")