from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UiAutomation"]

class UiAutomation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/UiAutomation"
    FLAG_DONT_SUPPRESS_ACCESSIBILITY_SERVICES = JavaStaticField("I")
    FLAG_DONT_USE_ACCESSIBILITY = JavaStaticField("I")
    ROTATION_FREEZE_0 = JavaStaticField("I")
    ROTATION_FREEZE_180 = JavaStaticField("I")
    ROTATION_FREEZE_270 = JavaStaticField("I")
    ROTATION_FREEZE_90 = JavaStaticField("I")
    ROTATION_FREEZE_CURRENT = JavaStaticField("I")
    ROTATION_UNFREEZE = JavaStaticField("I")
    setOnAccessibilityEventListener = JavaMethod("(Landroid/app/UiAutomation$OnAccessibilityEventListener;)V")
    clearCache = JavaMethod("()Z")
    adoptShellPermissionIdentity = JavaMultipleMethod([("()V", False, False), ("([Ljava/lang/String;)V", False, True)])
    dropShellPermissionIdentity = JavaMethod("()V")
    performGlobalAction = JavaMethod("(I)Z")
    findFocus = JavaMethod("(I)Landroid/view/accessibility/AccessibilityNodeInfo;")
    getServiceInfo = JavaMethod("()Landroid/accessibilityservice/AccessibilityServiceInfo;")
    setServiceInfo = JavaMethod("(Landroid/accessibilityservice/AccessibilityServiceInfo;)V")
    getWindows = JavaMethod("()Ljava/util/List;")
    getWindowsOnAllDisplays = JavaMethod("()Landroid/util/SparseArray;")
    getRootInActiveWindow = JavaMethod("()Landroid/view/accessibility/AccessibilityNodeInfo;")
    injectInputEvent = JavaMethod("(Landroid/view/InputEvent;Z)Z")
    setAnimationScale = JavaMethod("(F)V")
    setRotation = JavaMethod("(I)Z")
    executeAndWaitForEvent = JavaMethod("(Ljava/lang/Runnable;Landroid/app/UiAutomation$AccessibilityEventFilter;J)Landroid/view/accessibility/AccessibilityEvent;")
    waitForIdle = JavaMethod("(JJ)V")
    takeScreenshot = JavaMultipleMethod([("()Landroid/graphics/Bitmap;", False, False), ("(Landroid/view/Window;)Landroid/graphics/Bitmap;", False, False)])
    setRunAsMonkey = JavaMethod("(Z)V")
    clearWindowContentFrameStats = JavaMethod("(I)Z")
    getWindowContentFrameStats = JavaMethod("(I)Landroid/view/WindowContentFrameStats;")
    clearWindowAnimationFrameStats = JavaMethod("()V")
    getWindowAnimationFrameStats = JavaMethod("()Landroid/view/WindowAnimationFrameStats;")
    grantRuntimePermission = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    grantRuntimePermissionAsUser = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/os/UserHandle;)V")
    revokeRuntimePermission = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    revokeRuntimePermissionAsUser = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/os/UserHandle;)V")
    executeShellCommand = JavaMethod("(Ljava/lang/String;)Landroid/os/ParcelFileDescriptor;")
    executeShellCommandRw = JavaMethod("(Ljava/lang/String;)[Landroid/os/ParcelFileDescriptor;")
    executeShellCommandRwe = JavaMethod("(Ljava/lang/String;)[Landroid/os/ParcelFileDescriptor;")
    toString = JavaMethod("()Ljava/lang/String;")

    class AccessibilityEventFilter(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/UiAutomation/AccessibilityEventFilter"
        accept = JavaMethod("(Landroid/view/accessibility/AccessibilityEvent;)Z")

    class OnAccessibilityEventListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/UiAutomation/OnAccessibilityEventListener"
        onAccessibilityEvent = JavaMethod("(Landroid/view/accessibility/AccessibilityEvent;)V")