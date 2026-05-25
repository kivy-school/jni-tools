from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CaptioningManager"]

class CaptioningManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/accessibility/CaptioningManager"
    isEnabled = JavaMethod("()Z")
    getLocale = JavaMethod("()Ljava/util/Locale;")
    getFontScale = JavaMethod("()F")
    getUserStyle = JavaMethod("()Landroid/view/accessibility/CaptioningManager$CaptionStyle;")
    isSystemAudioCaptioningEnabled = JavaMethod("()Z")
    isSystemAudioCaptioningUiEnabled = JavaMethod("()Z")
    addCaptioningChangeListener = JavaMethod("(Landroid/view/accessibility/CaptioningManager$CaptioningChangeListener;)V")
    removeCaptioningChangeListener = JavaMethod("(Landroid/view/accessibility/CaptioningManager$CaptioningChangeListener;)V")
    isCallCaptioningEnabled = JavaMethod("()Z")

    class CaptionStyle(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/accessibility/CaptioningManager/CaptionStyle"
        EDGE_TYPE_DEPRESSED = JavaStaticField("I")
        EDGE_TYPE_DROP_SHADOW = JavaStaticField("I")
        EDGE_TYPE_NONE = JavaStaticField("I")
        EDGE_TYPE_OUTLINE = JavaStaticField("I")
        EDGE_TYPE_RAISED = JavaStaticField("I")
        EDGE_TYPE_UNSPECIFIED = JavaStaticField("I")
        backgroundColor = JavaField("I")
        edgeColor = JavaField("I")
        edgeType = JavaField("I")
        foregroundColor = JavaField("I")
        windowColor = JavaField("I")
        hasBackgroundColor = JavaMethod("()Z")
        hasForegroundColor = JavaMethod("()Z")
        hasEdgeType = JavaMethod("()Z")
        hasEdgeColor = JavaMethod("()Z")
        hasWindowColor = JavaMethod("()Z")
        getTypeface = JavaMethod("()Landroid/graphics/Typeface;")

    class CaptioningChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/accessibility/CaptioningManager/CaptioningChangeListener"
        __javaconstructor__ = [("()V", False)]
        onEnabledChanged = JavaMethod("(Z)V")
        onUserStyleChanged = JavaMethod("(Landroid/view/accessibility/CaptioningManager$CaptionStyle;)V")
        onLocaleChanged = JavaMethod("(Ljava/util/Locale;)V")
        onFontScaleChanged = JavaMethod("(F)V")
        onSystemAudioCaptioningChanged = JavaMethod("(Z)V")
        onSystemAudioCaptioningUiChanged = JavaMethod("(Z)V")