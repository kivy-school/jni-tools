from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CaptioningManager"]

class CaptioningManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/accessibility/CaptioningManager"
    isEnabled = JavaMethod("()Z")
    getFontScale = JavaMethod("()F")
    addCaptioningChangeListener = JavaMethod("(Landroid/view/accessibility/CaptioningManager$CaptioningChangeListener;)V")
    isCallCaptioningEnabled = JavaMethod("()Z")
    isSystemAudioCaptioningEnabled = JavaMethod("()Z")
    isSystemAudioCaptioningUiEnabled = JavaMethod("()Z")
    removeCaptioningChangeListener = JavaMethod("(Landroid/view/accessibility/CaptioningManager$CaptioningChangeListener;)V")
    getUserStyle = JavaMethod("()Landroid/view/accessibility/CaptioningManager$CaptionStyle;")
    getLocale = JavaMethod("()Ljava/util/Locale;")

    class CaptioningChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/accessibility/CaptioningManager$CaptioningChangeListener"
        __javaconstructor__ = [("()V", False)]
        onUserStyleChanged = JavaMethod("(Landroid/view/accessibility/CaptioningManager$CaptionStyle;)V")
        onSystemAudioCaptioningChanged = JavaMethod("(Z)V")
        onSystemAudioCaptioningUiChanged = JavaMethod("(Z)V")
        onLocaleChanged = JavaMethod("(Ljava/util/Locale;)V")
        onFontScaleChanged = JavaMethod("(F)V")
        onEnabledChanged = JavaMethod("(Z)V")

    class CaptionStyle(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/accessibility/CaptioningManager$CaptionStyle"
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
        hasEdgeColor = JavaMethod("()Z")
        hasEdgeType = JavaMethod("()Z")
        hasForegroundColor = JavaMethod("()Z")
        hasWindowColor = JavaMethod("()Z")
        getTypeface = JavaMethod("()Landroid/graphics/Typeface;")