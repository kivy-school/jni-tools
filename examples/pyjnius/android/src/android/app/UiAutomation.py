from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    toString = JavaMethod("()Ljava/lang/String;")
    findFocus = JavaMethod("(I)Landroid/view/accessibility/AccessibilityNodeInfo;")
    setRotation = JavaMethod("(I)Z")
    getServiceInfo = JavaMethod("()Landroid/accessibilityservice/AccessibilityServiceInfo;")
    clearCache = JavaMethod("()Z")
    injectInputEvent = JavaMethod("(Landroid/view/InputEvent;Z)Z")
    adoptShellPermissionIdentity = JavaMultipleMethod([("()V", False, False), ("([Ljava/lang/String;)V", False, True)])
    clearWindowAnimationFrameStats = JavaMethod("()V")
    clearWindowContentFrameStats = JavaMethod("(I)Z")
    dropShellPermissionIdentity = JavaMethod("()V")
    executeAndWaitForEvent = JavaMethod("(Ljava/lang/Runnable;Landroid/app/UiAutomation$AccessibilityEventFilter;J)Landroid/view/accessibility/AccessibilityEvent;")
    performGlobalAction = JavaMethod("(I)Z")
    revokeRuntimePermission = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    revokeRuntimePermissionAsUser = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/os/UserHandle;)V")
    setOnAccessibilityEventListener = JavaMethod("(Landroid/app/UiAutomation$OnAccessibilityEventListener;)V")
    setRunAsMonkey = JavaMethod("(Z)V")
    waitForIdle = JavaMethod("(JJ)V")
    takeScreenshot = JavaMultipleMethod([("(Landroid/view/Window;)Landroid/graphics/Bitmap;", False, False), ("()Landroid/graphics/Bitmap;", False, False)])
    getWindows = JavaMethod("()Ljava/util/List;")
    setServiceInfo = JavaMethod("(Landroid/accessibilityservice/AccessibilityServiceInfo;)V")
    getWindowAnimationFrameStats = JavaMethod("()Landroid/view/WindowAnimationFrameStats;")
    getWindowContentFrameStats = JavaMethod("(I)Landroid/view/WindowContentFrameStats;")
    getWindowsOnAllDisplays = JavaMethod("()Landroid/util/SparseArray;")
    grantRuntimePermission = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    grantRuntimePermissionAsUser = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/os/UserHandle;)V")
    setAnimationScale = JavaMethod("(F)V")
    executeShellCommand = JavaMethod("(Ljava/lang/String;)Landroid/os/ParcelFileDescriptor;")
    executeShellCommandRw = JavaMethod("(Ljava/lang/String;)[Landroid/os/ParcelFileDescriptor;")
    executeShellCommandRwe = JavaMethod("(Ljava/lang/String;)[Landroid/os/ParcelFileDescriptor;")
    getRootInActiveWindow = JavaMethod("()Landroid/view/accessibility/AccessibilityNodeInfo;")

    class OnAccessibilityEventListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/UiAutomation$OnAccessibilityEventListener"
        onAccessibilityEvent = JavaMethod("(Landroid/view/accessibility/AccessibilityEvent;)V")

    class AccessibilityEventFilter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/UiAutomation$AccessibilityEventFilter"
        accept = JavaMethod("(Landroid/view/accessibility/AccessibilityEvent;)Z")