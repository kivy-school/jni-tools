from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    add = JavaMultipleMethod([("(Landroid/app/Fragment;Ljava/lang/String;)Landroid/app/FragmentTransaction;", False, False), ("(ILandroid/app/Fragment;)Landroid/app/FragmentTransaction;", False, False), ("(ILandroid/app/Fragment;Ljava/lang/String;)Landroid/app/FragmentTransaction;", False, False)])
    replace = JavaMultipleMethod([("(ILandroid/app/Fragment;)Landroid/app/FragmentTransaction;", False, False), ("(ILandroid/app/Fragment;Ljava/lang/String;)Landroid/app/FragmentTransaction;", False, False)])
    remove = JavaMethod("(Landroid/app/Fragment;)Landroid/app/FragmentTransaction;")
    hide = JavaMethod("(Landroid/app/Fragment;)Landroid/app/FragmentTransaction;")
    show = JavaMethod("(Landroid/app/Fragment;)Landroid/app/FragmentTransaction;")
    detach = JavaMethod("(Landroid/app/Fragment;)Landroid/app/FragmentTransaction;")
    attach = JavaMethod("(Landroid/app/Fragment;)Landroid/app/FragmentTransaction;")
    setPrimaryNavigationFragment = JavaMethod("(Landroid/app/Fragment;)Landroid/app/FragmentTransaction;")
    isEmpty = JavaMethod("()Z")
    setCustomAnimations = JavaMultipleMethod([("(II)Landroid/app/FragmentTransaction;", False, False), ("(IIII)Landroid/app/FragmentTransaction;", False, False)])
    setTransition = JavaMethod("(I)Landroid/app/FragmentTransaction;")
    addSharedElement = JavaMethod("(Landroid/view/View;Ljava/lang/String;)Landroid/app/FragmentTransaction;")
    setTransitionStyle = JavaMethod("(I)Landroid/app/FragmentTransaction;")
    addToBackStack = JavaMethod("(Ljava/lang/String;)Landroid/app/FragmentTransaction;")
    isAddToBackStackAllowed = JavaMethod("()Z")
    disallowAddToBackStack = JavaMethod("()Landroid/app/FragmentTransaction;")
    setBreadCrumbTitle = JavaMultipleMethod([("(I)Landroid/app/FragmentTransaction;", False, False), ("(Ljava/lang/CharSequence;)Landroid/app/FragmentTransaction;", False, False)])
    setBreadCrumbShortTitle = JavaMultipleMethod([("(I)Landroid/app/FragmentTransaction;", False, False), ("(Ljava/lang/CharSequence;)Landroid/app/FragmentTransaction;", False, False)])
    setReorderingAllowed = JavaMethod("(Z)Landroid/app/FragmentTransaction;")
    runOnCommit = JavaMethod("(Ljava/lang/Runnable;)Landroid/app/FragmentTransaction;")
    commit = JavaMethod("()I")
    commitAllowingStateLoss = JavaMethod("()I")
    commitNow = JavaMethod("()V")
    commitNowAllowingStateLoss = JavaMethod("()V")