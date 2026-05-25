from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TabHost"]

class TabHost(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/TabHost"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    newTabSpec = JavaMethod("(Ljava/lang/String;)Landroid/widget/TabHost$TabSpec;")
    setup = JavaMultipleMethod([("()V", False, False), ("(Landroid/app/LocalActivityManager;)V", False, False)])
    onTouchModeChanged = JavaMethod("(Z)V")
    addTab = JavaMethod("(Landroid/widget/TabHost$TabSpec;)V")
    clearAllTabs = JavaMethod("()V")
    getTabWidget = JavaMethod("()Landroid/widget/TabWidget;")
    getCurrentTab = JavaMethod("()I")
    getCurrentTabTag = JavaMethod("()Ljava/lang/String;")
    getCurrentTabView = JavaMethod("()Landroid/view/View;")
    getCurrentView = JavaMethod("()Landroid/view/View;")
    setCurrentTabByTag = JavaMethod("(Ljava/lang/String;)V")
    getTabContentView = JavaMethod("()Landroid/widget/FrameLayout;")
    dispatchKeyEvent = JavaMethod("(Landroid/view/KeyEvent;)Z")
    dispatchWindowFocusChanged = JavaMethod("(Z)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    setCurrentTab = JavaMethod("(I)V")
    setOnTabChangedListener = JavaMethod("(Landroid/widget/TabHost$OnTabChangeListener;)V")

    class OnTabChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/TabHost/OnTabChangeListener"
        onTabChanged = JavaMethod("(Ljava/lang/String;)V")

    class TabContentFactory(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/TabHost/TabContentFactory"
        createTabContent = JavaMethod("(Ljava/lang/String;)Landroid/view/View;")

    class TabSpec(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/TabHost/TabSpec"
        setIndicator = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Landroid/widget/TabHost$TabSpec;", False, False), ("(Ljava/lang/CharSequence;Landroid/graphics/drawable/Drawable;)Landroid/widget/TabHost$TabSpec;", False, False), ("(Landroid/view/View;)Landroid/widget/TabHost$TabSpec;", False, False)])
        setContent = JavaMultipleMethod([("(I)Landroid/widget/TabHost$TabSpec;", False, False), ("(Landroid/widget/TabHost$TabContentFactory;)Landroid/widget/TabHost$TabSpec;", False, False), ("(Landroid/content/Intent;)Landroid/widget/TabHost$TabSpec;", False, False)])
        getTag = JavaMethod("()Ljava/lang/String;")