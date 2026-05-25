from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FragmentManager"]

class FragmentManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/FragmentManager"
    __javaconstructor__ = [("()V", False)]
    POP_BACK_STACK_INCLUSIVE = JavaStaticField("I")
    beginTransaction = JavaMethod("()Landroid/app/FragmentTransaction;")
    executePendingTransactions = JavaMethod("()Z")
    findFragmentById = JavaMethod("(I)Landroid/app/Fragment;")
    findFragmentByTag = JavaMethod("(Ljava/lang/String;)Landroid/app/Fragment;")
    popBackStack = JavaMultipleMethod([("()V", False, False), ("(Ljava/lang/String;I)V", False, False), ("(II)V", False, False)])
    popBackStackImmediate = JavaMultipleMethod([("()Z", False, False), ("(Ljava/lang/String;I)Z", False, False), ("(II)Z", False, False)])
    getBackStackEntryCount = JavaMethod("()I")
    getBackStackEntryAt = JavaMethod("(I)Landroid/app/FragmentManager$BackStackEntry;")
    addOnBackStackChangedListener = JavaMethod("(Landroid/app/FragmentManager$OnBackStackChangedListener;)V")
    removeOnBackStackChangedListener = JavaMethod("(Landroid/app/FragmentManager$OnBackStackChangedListener;)V")
    putFragment = JavaMethod("(Landroid/os/Bundle;Ljava/lang/String;Landroid/app/Fragment;)V")
    getFragment = JavaMethod("(Landroid/os/Bundle;Ljava/lang/String;)Landroid/app/Fragment;")
    getFragments = JavaMethod("()Ljava/util/List;")
    saveFragmentInstanceState = JavaMethod("(Landroid/app/Fragment;)Landroid/app/Fragment$SavedState;")
    isDestroyed = JavaMethod("()Z")
    registerFragmentLifecycleCallbacks = JavaMethod("(Landroid/app/FragmentManager$FragmentLifecycleCallbacks;Z)V")
    unregisterFragmentLifecycleCallbacks = JavaMethod("(Landroid/app/FragmentManager$FragmentLifecycleCallbacks;)V")
    getPrimaryNavigationFragment = JavaMethod("()Landroid/app/Fragment;")
    dump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
    enableDebugLogging = JavaStaticMethod("(Z)V")
    invalidateOptionsMenu = JavaMethod("()V")
    isStateSaved = JavaMethod("()Z")

    class BackStackEntry(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/FragmentManager/BackStackEntry"
        getId = JavaMethod("()I")
        getName = JavaMethod("()Ljava/lang/String;")
        getBreadCrumbTitleRes = JavaMethod("()I")
        getBreadCrumbShortTitleRes = JavaMethod("()I")
        getBreadCrumbTitle = JavaMethod("()Ljava/lang/CharSequence;")
        getBreadCrumbShortTitle = JavaMethod("()Ljava/lang/CharSequence;")

    class FragmentLifecycleCallbacks(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/FragmentManager/FragmentLifecycleCallbacks"
        __javaconstructor__ = [("()V", False)]
        onFragmentPreAttached = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/content/Context;)V")
        onFragmentAttached = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/content/Context;)V")
        onFragmentPreCreated = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/os/Bundle;)V")
        onFragmentCreated = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/os/Bundle;)V")
        onFragmentActivityCreated = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/os/Bundle;)V")
        onFragmentViewCreated = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/view/View;Landroid/os/Bundle;)V")
        onFragmentStarted = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")
        onFragmentResumed = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")
        onFragmentPaused = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")
        onFragmentStopped = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")
        onFragmentSaveInstanceState = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/os/Bundle;)V")
        onFragmentViewDestroyed = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")
        onFragmentDestroyed = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")
        onFragmentDetached = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")

    class OnBackStackChangedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/FragmentManager/OnBackStackChangedListener"
        onBackStackChanged = JavaMethod("()V")