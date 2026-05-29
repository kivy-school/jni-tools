from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FragmentManager"]

class FragmentManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/FragmentManager"
    __javaconstructor__ = [("()V", False)]
    POP_BACK_STACK_INCLUSIVE = JavaStaticField("I")
    isStateSaved = JavaMethod("()Z")
    enableDebugLogging = JavaStaticMethod("(Z)V")
    addOnBackStackChangedListener = JavaMethod("(Landroid/app/FragmentManager$OnBackStackChangedListener;)V")
    executePendingTransactions = JavaMethod("()Z")
    findFragmentById = JavaMethod("(I)Landroid/app/Fragment;")
    findFragmentByTag = JavaMethod("(Ljava/lang/String;)Landroid/app/Fragment;")
    getBackStackEntryAt = JavaMethod("(I)Landroid/app/FragmentManager$BackStackEntry;")
    getBackStackEntryCount = JavaMethod("()I")
    getFragments = JavaMethod("()Ljava/util/List;")
    getPrimaryNavigationFragment = JavaMethod("()Landroid/app/Fragment;")
    popBackStack = JavaMultipleMethod([("(II)V", False, False), ("()V", False, False), ("(Ljava/lang/String;I)V", False, False)])
    popBackStackImmediate = JavaMultipleMethod([("()Z", False, False), ("(II)Z", False, False), ("(Ljava/lang/String;I)Z", False, False)])
    putFragment = JavaMethod("(Landroid/os/Bundle;Ljava/lang/String;Landroid/app/Fragment;)V")
    registerFragmentLifecycleCallbacks = JavaMethod("(Landroid/app/FragmentManager$FragmentLifecycleCallbacks;Z)V")
    removeOnBackStackChangedListener = JavaMethod("(Landroid/app/FragmentManager$OnBackStackChangedListener;)V")
    saveFragmentInstanceState = JavaMethod("(Landroid/app/Fragment;)Landroid/app/Fragment$SavedState;")
    unregisterFragmentLifecycleCallbacks = JavaMethod("(Landroid/app/FragmentManager$FragmentLifecycleCallbacks;)V")
    isDestroyed = JavaMethod("()Z")
    dump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
    invalidateOptionsMenu = JavaMethod("()V")
    beginTransaction = JavaMethod("()Landroid/app/FragmentTransaction;")
    getFragment = JavaMethod("(Landroid/os/Bundle;Ljava/lang/String;)Landroid/app/Fragment;")

    class OnBackStackChangedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/FragmentManager$OnBackStackChangedListener"
        onBackStackChanged = JavaMethod("()V")

    class FragmentLifecycleCallbacks(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/FragmentManager$FragmentLifecycleCallbacks"
        __javaconstructor__ = [("()V", False)]
        onFragmentCreated = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/os/Bundle;)V")
        onFragmentStopped = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")
        onFragmentDetached = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")
        onFragmentAttached = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/content/Context;)V")
        onFragmentResumed = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")
        onFragmentPaused = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")
        onFragmentActivityCreated = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/os/Bundle;)V")
        onFragmentDestroyed = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")
        onFragmentStarted = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")
        onFragmentPreAttached = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/content/Context;)V")
        onFragmentPreCreated = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/os/Bundle;)V")
        onFragmentSaveInstanceState = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/os/Bundle;)V")
        onFragmentViewCreated = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;Landroid/view/View;Landroid/os/Bundle;)V")
        onFragmentViewDestroyed = JavaMethod("(Landroid/app/FragmentManager;Landroid/app/Fragment;)V")

    class BackStackEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/FragmentManager$BackStackEntry"
        getBreadCrumbShortTitle = JavaMethod("()Ljava/lang/CharSequence;")
        getBreadCrumbShortTitleRes = JavaMethod("()I")
        getBreadCrumbTitle = JavaMethod("()Ljava/lang/CharSequence;")
        getBreadCrumbTitleRes = JavaMethod("()I")
        getName = JavaMethod("()Ljava/lang/String;")
        getId = JavaMethod("()I")