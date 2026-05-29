from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessibilityManager"]

class AccessibilityManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/accessibility/AccessibilityManager"
    FLAG_CONTENT_CONTROLS = JavaStaticField("I")
    FLAG_CONTENT_ICONS = JavaStaticField("I")
    FLAG_CONTENT_TEXT = JavaStaticField("I")
    addAccessibilityRequestPreparer = JavaMethod("(Landroid/view/accessibility/AccessibilityRequestPreparer;)V")
    addAccessibilityServicesStateChangeListener = JavaMultipleMethod([("(Landroid/view/accessibility/AccessibilityManager$AccessibilityServicesStateChangeListener;)V", False, False), ("(Ljava/util/concurrent/Executor;Landroid/view/accessibility/AccessibilityManager$AccessibilityServicesStateChangeListener;)V", False, False)])
    addAccessibilityStateChangeListener = JavaMultipleMethod([("(Landroid/view/accessibility/AccessibilityManager$AccessibilityStateChangeListener;Landroid/os/Handler;)V", False, False), ("(Landroid/view/accessibility/AccessibilityManager$AccessibilityStateChangeListener;)Z", False, False)])
    addAudioDescriptionRequestedChangeListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/view/accessibility/AccessibilityManager$AudioDescriptionRequestedChangeListener;)V")
    addHighContrastTextStateChangeListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/view/accessibility/AccessibilityManager$HighContrastTextStateChangeListener;)V")
    addTouchExplorationStateChangeListener = JavaMultipleMethod([("(Landroid/view/accessibility/AccessibilityManager$TouchExplorationStateChangeListener;Landroid/os/Handler;)V", False, False), ("(Landroid/view/accessibility/AccessibilityManager$TouchExplorationStateChangeListener;)Z", False, False)])
    getAccessibilityFocusColor = JavaMethod("()I")
    getAccessibilityFocusStrokeWidth = JavaMethod("()I")
    getAccessibilityServiceList = JavaMethod("()Ljava/util/List;")
    getEnabledAccessibilityServiceList = JavaMethod("(I)Ljava/util/List;")
    getInstalledAccessibilityServiceList = JavaMethod("()Ljava/util/List;")
    getRecommendedTimeoutMillis = JavaMethod("(II)I")
    isAccessibilityButtonSupported = JavaStaticMethod("()Z")
    isAudioDescriptionRequested = JavaMethod("()Z")
    isHighContrastTextEnabled = JavaMethod("()Z")
    isRequestFromAccessibilityTool = JavaMethod("()Z")
    isTouchExplorationEnabled = JavaMethod("()Z")
    removeAccessibilityRequestPreparer = JavaMethod("(Landroid/view/accessibility/AccessibilityRequestPreparer;)V")
    removeAccessibilityServicesStateChangeListener = JavaMethod("(Landroid/view/accessibility/AccessibilityManager$AccessibilityServicesStateChangeListener;)Z")
    removeAccessibilityStateChangeListener = JavaMethod("(Landroid/view/accessibility/AccessibilityManager$AccessibilityStateChangeListener;)Z")
    removeAudioDescriptionRequestedChangeListener = JavaMethod("(Landroid/view/accessibility/AccessibilityManager$AudioDescriptionRequestedChangeListener;)Z")
    removeHighContrastTextStateChangeListener = JavaMethod("(Landroid/view/accessibility/AccessibilityManager$HighContrastTextStateChangeListener;)V")
    removeTouchExplorationStateChangeListener = JavaMethod("(Landroid/view/accessibility/AccessibilityManager$TouchExplorationStateChangeListener;)Z")
    interrupt = JavaMethod("()V")
    isEnabled = JavaMethod("()Z")
    sendAccessibilityEvent = JavaMethod("(Landroid/view/accessibility/AccessibilityEvent;)V")

    class TouchExplorationStateChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/accessibility/AccessibilityManager$TouchExplorationStateChangeListener"
        onTouchExplorationStateChanged = JavaMethod("(Z)V")

    class HighContrastTextStateChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/accessibility/AccessibilityManager$HighContrastTextStateChangeListener"
        onHighContrastTextStateChanged = JavaMethod("(Z)V")

    class AudioDescriptionRequestedChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/accessibility/AccessibilityManager$AudioDescriptionRequestedChangeListener"
        onAudioDescriptionRequestedChanged = JavaMethod("(Z)V")

    class AccessibilityStateChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/accessibility/AccessibilityManager$AccessibilityStateChangeListener"
        onAccessibilityStateChanged = JavaMethod("(Z)V")

    class AccessibilityServicesStateChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/accessibility/AccessibilityManager$AccessibilityServicesStateChangeListener"
        onAccessibilityServicesStateChanged = JavaMethod("(Landroid/view/accessibility/AccessibilityManager;)V")