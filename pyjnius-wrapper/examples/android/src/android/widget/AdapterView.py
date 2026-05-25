from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdapterView"]

class AdapterView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/AdapterView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    INVALID_POSITION = JavaStaticField("I")
    INVALID_ROW_ID = JavaStaticField("J")
    ITEM_VIEW_TYPE_HEADER_OR_FOOTER = JavaStaticField("I")
    ITEM_VIEW_TYPE_IGNORE = JavaStaticField("I")
    setOnItemClickListener = JavaMethod("(Landroid/widget/AdapterView$OnItemClickListener;)V")
    getOnItemClickListener = JavaMethod("()Landroid/widget/AdapterView$OnItemClickListener;")
    performItemClick = JavaMethod("(Landroid/view/View;IJ)Z")
    setOnItemLongClickListener = JavaMethod("(Landroid/widget/AdapterView$OnItemLongClickListener;)V")
    getOnItemLongClickListener = JavaMethod("()Landroid/widget/AdapterView$OnItemLongClickListener;")
    setOnItemSelectedListener = JavaMethod("(Landroid/widget/AdapterView$OnItemSelectedListener;)V")
    getOnItemSelectedListener = JavaMethod("()Landroid/widget/AdapterView$OnItemSelectedListener;")
    getAdapter = JavaMethod("()Landroid/widget/Adapter;")
    setAdapter = JavaMethod("(Landroid/widget/Adapter;)V")
    addView = JavaMultipleMethod([("(Landroid/view/View;)V", False, False), ("(Landroid/view/View;I)V", False, False), ("(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V", False, False), ("(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V", False, False)])
    removeView = JavaMethod("(Landroid/view/View;)V")
    removeViewAt = JavaMethod("(I)V")
    removeAllViews = JavaMethod("()V")
    onLayout = JavaMethod("(ZIIII)V")
    getSelectedItemPosition = JavaMethod("()I")
    getSelectedItemId = JavaMethod("()J")
    getSelectedView = JavaMethod("()Landroid/view/View;")
    getSelectedItem = JavaMethod("()Ljava/lang/Object;")
    getCount = JavaMethod("()I")
    getPositionForView = JavaMethod("(Landroid/view/View;)I")
    getFirstVisiblePosition = JavaMethod("()I")
    getLastVisiblePosition = JavaMethod("()I")
    setSelection = JavaMethod("(I)V")
    setEmptyView = JavaMethod("(Landroid/view/View;)V")
    getEmptyView = JavaMethod("()Landroid/view/View;")
    setFocusable = JavaMethod("(I)V")
    setFocusableInTouchMode = JavaMethod("(Z)V")
    getItemAtPosition = JavaMethod("(I)Ljava/lang/Object;")
    getItemIdAtPosition = JavaMethod("(I)J")
    setOnClickListener = JavaMethod("(Landroid/view/View$OnClickListener;)V")
    dispatchSaveInstanceState = JavaMethod("(Landroid/util/SparseArray;)V")
    dispatchRestoreInstanceState = JavaMethod("(Landroid/util/SparseArray;)V")
    onDetachedFromWindow = JavaMethod("()V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    canAnimate = JavaMethod("()Z")
    onProvideAutofillStructure = JavaMethod("(Landroid/view/ViewStructure;I)V")

    class AdapterContextMenuInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/AdapterView/AdapterContextMenuInfo"
        __javaconstructor__ = [("(Landroid/view/View;IJ)V", False)]
        id = JavaField("J")
        position = JavaField("I")
        targetView = JavaField("Landroid/view/View;")

    class OnItemClickListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/AdapterView/OnItemClickListener"
        onItemClick = JavaMethod("(Landroid/widget/AdapterView;Landroid/view/View;IJ)V")

    class OnItemLongClickListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/AdapterView/OnItemLongClickListener"
        onItemLongClick = JavaMethod("(Landroid/widget/AdapterView;Landroid/view/View;IJ)Z")

    class OnItemSelectedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/AdapterView/OnItemSelectedListener"
        onItemSelected = JavaMethod("(Landroid/widget/AdapterView;Landroid/view/View;IJ)V")
        onNothingSelected = JavaMethod("(Landroid/widget/AdapterView;)V")