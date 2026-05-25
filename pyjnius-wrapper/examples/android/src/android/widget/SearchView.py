from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchView"]

class SearchView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/SearchView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    setSearchableInfo = JavaMethod("(Landroid/app/SearchableInfo;)V")
    setImeOptions = JavaMethod("(I)V")
    getImeOptions = JavaMethod("()I")
    setInputType = JavaMethod("(I)V")
    getInputType = JavaMethod("()I")
    requestFocus = JavaMethod("(ILandroid/graphics/Rect;)Z")
    clearFocus = JavaMethod("()V")
    setOnQueryTextListener = JavaMethod("(Landroid/widget/SearchView$OnQueryTextListener;)V")
    setOnCloseListener = JavaMethod("(Landroid/widget/SearchView$OnCloseListener;)V")
    setOnQueryTextFocusChangeListener = JavaMethod("(Landroid/view/View$OnFocusChangeListener;)V")
    setOnSuggestionListener = JavaMethod("(Landroid/widget/SearchView$OnSuggestionListener;)V")
    setOnSearchClickListener = JavaMethod("(Landroid/view/View$OnClickListener;)V")
    getQuery = JavaMethod("()Ljava/lang/CharSequence;")
    setQuery = JavaMethod("(Ljava/lang/CharSequence;Z)V")
    setQueryHint = JavaMethod("(Ljava/lang/CharSequence;)V")
    getQueryHint = JavaMethod("()Ljava/lang/CharSequence;")
    setIconifiedByDefault = JavaMethod("(Z)V")
    isIconfiedByDefault = JavaMethod("()Z")
    isIconifiedByDefault = JavaMethod("()Z")
    setIconified = JavaMethod("(Z)V")
    isIconified = JavaMethod("()Z")
    setSubmitButtonEnabled = JavaMethod("(Z)V")
    isSubmitButtonEnabled = JavaMethod("()Z")
    setQueryRefinementEnabled = JavaMethod("(Z)V")
    isQueryRefinementEnabled = JavaMethod("()Z")
    setSuggestionsAdapter = JavaMethod("(Landroid/widget/CursorAdapter;)V")
    getSuggestionsAdapter = JavaMethod("()Landroid/widget/CursorAdapter;")
    setMaxWidth = JavaMethod("(I)V")
    getMaxWidth = JavaMethod("()I")
    onMeasure = JavaMethod("(II)V")
    onLayout = JavaMethod("(ZIIII)V")
    onDetachedFromWindow = JavaMethod("()V")
    onKeyDown = JavaMethod("(ILandroid/view/KeyEvent;)Z")
    onWindowFocusChanged = JavaMethod("(Z)V")
    onActionViewCollapsed = JavaMethod("()V")
    onActionViewExpanded = JavaMethod("()V")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Parcelable;)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")

    class OnCloseListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SearchView/OnCloseListener"
        onClose = JavaMethod("()Z")

    class OnQueryTextListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SearchView/OnQueryTextListener"
        onQueryTextSubmit = JavaMethod("(Ljava/lang/String;)Z")
        onQueryTextChange = JavaMethod("(Ljava/lang/String;)Z")

    class OnSuggestionListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SearchView/OnSuggestionListener"
        onSuggestionSelect = JavaMethod("(I)Z")
        onSuggestionClick = JavaMethod("(I)Z")