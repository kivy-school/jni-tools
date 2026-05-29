from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FragmentTransaction"]

class FragmentTransaction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/FragmentTransaction"
    __javaconstructor__ = [("()V", False)]
    TRANSIT_ENTER_MASK = JavaStaticField("I")
    TRANSIT_EXIT_MASK = JavaStaticField("I")
    TRANSIT_FRAGMENT_CLOSE = JavaStaticField("I")
    TRANSIT_FRAGMENT_FADE = JavaStaticField("I")
    TRANSIT_FRAGMENT_OPEN = JavaStaticField("I")
    TRANSIT_NONE = JavaStaticField("I")
    TRANSIT_UNSET = JavaStaticField("I")
    setTransition = JavaMethod("(I)Landroid/app/FragmentTransaction;")
    addToBackStack = JavaMethod("(Ljava/lang/String;)Landroid/app/FragmentTransaction;")
    commitAllowingStateLoss = JavaMethod("()I")
    commitNow = JavaMethod("()V")
    commitNowAllowingStateLoss = JavaMethod("()V")
    runOnCommit = JavaMethod("(Ljava/lang/Runnable;)Landroid/app/FragmentTransaction;")
    disallowAddToBackStack = JavaMethod("()Landroid/app/FragmentTransaction;")
    isAddToBackStackAllowed = JavaMethod("()Z")
    setBreadCrumbShortTitle = JavaMultipleMethod([("(I)Landroid/app/FragmentTransaction;", False, False), ("(Ljava/lang/CharSequence;)Landroid/app/FragmentTransaction;", False, False)])
    setBreadCrumbTitle = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Landroid/app/FragmentTransaction;", False, False), ("(I)Landroid/app/FragmentTransaction;", False, False)])
    setCustomAnimations = JavaMultipleMethod([("(IIII)Landroid/app/FragmentTransaction;", False, False), ("(II)Landroid/app/FragmentTransaction;", False, False)])
    setPrimaryNavigationFragment = JavaMethod("(Landroid/app/Fragment;)Landroid/app/FragmentTransaction;")
    setReorderingAllowed = JavaMethod("(Z)Landroid/app/FragmentTransaction;")
    setTransitionStyle = JavaMethod("(I)Landroid/app/FragmentTransaction;")
    remove = JavaMethod("(Landroid/app/Fragment;)Landroid/app/FragmentTransaction;")
    commit = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    replace = JavaMultipleMethod([("(ILandroid/app/Fragment;Ljava/lang/String;)Landroid/app/FragmentTransaction;", False, False), ("(ILandroid/app/Fragment;)Landroid/app/FragmentTransaction;", False, False)])
    add = JavaMultipleMethod([("(ILandroid/app/Fragment;)Landroid/app/FragmentTransaction;", False, False), ("(Landroid/app/Fragment;Ljava/lang/String;)Landroid/app/FragmentTransaction;", False, False), ("(ILandroid/app/Fragment;Ljava/lang/String;)Landroid/app/FragmentTransaction;", False, False)])
    hide = JavaMethod("(Landroid/app/Fragment;)Landroid/app/FragmentTransaction;")
    show = JavaMethod("(Landroid/app/Fragment;)Landroid/app/FragmentTransaction;")
    attach = JavaMethod("(Landroid/app/Fragment;)Landroid/app/FragmentTransaction;")
    addSharedElement = JavaMethod("(Landroid/view/View;Ljava/lang/String;)Landroid/app/FragmentTransaction;")
    detach = JavaMethod("(Landroid/app/Fragment;)Landroid/app/FragmentTransaction;")