from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessibilityManager"]

class AccessibilityManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/accessibility/AccessibilityManager"
    FLAG_CONTENT_CONTROLS = JavaStaticField("I")
    FLAG_CONTENT_ICONS = JavaStaticField("I")
    FLAG_CONTENT_TEXT = JavaStaticField("I")
    isEnabled = JavaMethod("()Z")
    isTouchExplorationEnabled = JavaMethod("()Z")
    sendAccessibilityEvent = JavaMethod("(Landroid/view/accessibility/AccessibilityEvent;)V")
    interrupt = JavaMethod("()V")
    getAccessibilityServiceList = JavaMethod("()Ljava/util/List;")
    getInstalledAccessibilityServiceList = JavaMethod("()Ljava/util/List;")
    getEnabledAccessibilityServiceList = JavaMethod("(I)Ljava/util/List;")
    addAccessibilityStateChangeListener = JavaMultipleMethod([("(Landroid/view/accessibility/AccessibilityManager$AccessibilityStateChangeListener;)Z", False, False), ("(Landroid/view/accessibility/AccessibilityManager$AccessibilityStateChangeListener;Landroid/os/Handler;)V", False, False)])
    removeAccessibilityStateChangeListener = JavaMethod("(Landroid/view/accessibility/AccessibilityManager$AccessibilityStateChangeListener;)Z")
    addTouchExplorationStateChangeListener = JavaMultipleMethod([("(Landroid/view/accessibility/AccessibilityManager$TouchExplorationStateChangeListener;)Z", False, False), ("(Landroid/view/accessibility/AccessibilityManager$TouchExplorationStateChangeListener;Landroid/os/Handler;)V", False, False)])
    removeTouchExplorationStateChangeListener = JavaMethod("(Landroid/view/accessibility/AccessibilityManager$TouchExplorationStateChangeListener;)Z")
    addAccessibilityServicesStateChangeListener = JavaMultipleMethod([("(Ljava/util/concurrent/Executor;Landroid/view/accessibility/AccessibilityManager$AccessibilityServicesStateChangeListener;)V", False, False), ("(Landroid/view/accessibility/AccessibilityManager$AccessibilityServicesStateChangeListener;)V", False, False)])
    removeAccessibilityServicesStateChangeListener = JavaMethod("(Landroid/view/accessibility/AccessibilityManager$AccessibilityServicesStateChangeListener;)Z")
    isRequestFromAccessibilityTool = JavaMethod("()Z")
    addAccessibilityRequestPreparer = JavaMethod("(Landroid/view/accessibility/AccessibilityRequestPreparer;)V")
    removeAccessibilityRequestPreparer = JavaMethod("(Landroid/view/accessibility/AccessibilityRequestPreparer;)V")
    getRecommendedTimeoutMillis = JavaMethod("(II)I")
    getAccessibilityFocusStrokeWidth = JavaMethod("()I")
    getAccessibilityFocusColor = JavaMethod("()I")
    addAudioDescriptionRequestedChangeListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/view/accessibility/AccessibilityManager$AudioDescriptionRequestedChangeListener;)V")
    removeAudioDescriptionRequestedChangeListener = JavaMethod("(Landroid/view/accessibility/AccessibilityManager$AudioDescriptionRequestedChangeListener;)Z")
    isAudioDescriptionRequested = JavaMethod("()Z")
    isAccessibilityButtonSupported = JavaStaticMethod("()Z")

    class AccessibilityServicesStateChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/accessibility/AccessibilityManager/AccessibilityServicesStateChangeListener"
        onAccessibilityServicesStateChanged = JavaMethod("(Landroid/view/accessibility/AccessibilityManager;)V")

    class AccessibilityStateChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/accessibility/AccessibilityManager/AccessibilityStateChangeListener"
        onAccessibilityStateChanged = JavaMethod("(Z)V")

    class AudioDescriptionRequestedChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/accessibility/AccessibilityManager/AudioDescriptionRequestedChangeListener"
        onAudioDescriptionRequestedChanged = JavaMethod("(Z)V")

    class TouchExplorationStateChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/accessibility/AccessibilityManager/TouchExplorationStateChangeListener"
        onTouchExplorationStateChanged = JavaMethod("(Z)V")