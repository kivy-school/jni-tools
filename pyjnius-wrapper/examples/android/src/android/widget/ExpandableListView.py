from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExpandableListView"]

class ExpandableListView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ExpandableListView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    CHILD_INDICATOR_INHERIT = JavaStaticField("I")
    PACKED_POSITION_TYPE_CHILD = JavaStaticField("I")
    PACKED_POSITION_TYPE_GROUP = JavaStaticField("I")
    PACKED_POSITION_TYPE_NULL = JavaStaticField("I")
    PACKED_POSITION_VALUE_NULL = JavaStaticField("J")
    onRtlPropertiesChanged = JavaMethod("(I)V")
    dispatchDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
    setChildDivider = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    setAdapter = JavaMultipleMethod([("(Landroid/widget/ListAdapter;)V", False, False), ("(Landroid/widget/ExpandableListAdapter;)V", False, False)])
    getAdapter = JavaMethod("()Landroid/widget/ListAdapter;")
    setOnItemClickListener = JavaMethod("(Landroid/widget/AdapterView$OnItemClickListener;)V")
    getExpandableListAdapter = JavaMethod("()Landroid/widget/ExpandableListAdapter;")
    performItemClick = JavaMethod("(Landroid/view/View;IJ)Z")
    expandGroup = JavaMultipleMethod([("(I)Z", False, False), ("(IZ)Z", False, False)])
    collapseGroup = JavaMethod("(I)Z")
    setOnGroupCollapseListener = JavaMethod("(Landroid/widget/ExpandableListView$OnGroupCollapseListener;)V")
    setOnGroupExpandListener = JavaMethod("(Landroid/widget/ExpandableListView$OnGroupExpandListener;)V")
    setOnGroupClickListener = JavaMethod("(Landroid/widget/ExpandableListView$OnGroupClickListener;)V")
    setOnChildClickListener = JavaMethod("(Landroid/widget/ExpandableListView$OnChildClickListener;)V")
    getExpandableListPosition = JavaMethod("(I)J")
    getFlatListPosition = JavaMethod("(J)I")
    getSelectedPosition = JavaMethod("()J")
    getSelectedId = JavaMethod("()J")
    setSelectedGroup = JavaMethod("(I)V")
    setSelectedChild = JavaMethod("(IIZ)Z")
    isGroupExpanded = JavaMethod("(I)Z")
    getPackedPositionType = JavaStaticMethod("(J)I")
    getPackedPositionGroup = JavaStaticMethod("(J)I")
    getPackedPositionChild = JavaStaticMethod("(J)I")
    getPackedPositionForChild = JavaStaticMethod("(II)J")
    getPackedPositionForGroup = JavaStaticMethod("(I)J")
    onInitializeAccessibilityNodeInfoForItem = JavaMethod("(Landroid/view/View;ILandroid/view/accessibility/AccessibilityNodeInfo;)V")
    setChildIndicator = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    setChildIndicatorBounds = JavaMethod("(II)V")
    setChildIndicatorBoundsRelative = JavaMethod("(II)V")
    setGroupIndicator = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    setIndicatorBounds = JavaMethod("(II)V")
    setIndicatorBoundsRelative = JavaMethod("(II)V")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Parcelable;)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")

    class ExpandableListContextMenuInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/ExpandableListView/ExpandableListContextMenuInfo"
        __javaconstructor__ = [("(Landroid/view/View;JJ)V", False)]
        id = JavaField("J")
        packedPosition = JavaField("J")
        targetView = JavaField("Landroid/view/View;")

    class OnChildClickListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/ExpandableListView/OnChildClickListener"
        onChildClick = JavaMethod("(Landroid/widget/ExpandableListView;Landroid/view/View;IIJ)Z")

    class OnGroupClickListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/ExpandableListView/OnGroupClickListener"
        onGroupClick = JavaMethod("(Landroid/widget/ExpandableListView;Landroid/view/View;IJ)Z")

    class OnGroupCollapseListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/ExpandableListView/OnGroupCollapseListener"
        onGroupCollapse = JavaMethod("(I)V")

    class OnGroupExpandListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/ExpandableListView/OnGroupExpandListener"
        onGroupExpand = JavaMethod("(I)V")