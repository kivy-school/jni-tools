from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DisplayManager"]

class DisplayManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/display/DisplayManager"
    DISPLAY_CATEGORY_PRESENTATION = JavaStaticField("Ljava/lang/String;")
    MATCH_CONTENT_FRAMERATE_ALWAYS = JavaStaticField("I")
    MATCH_CONTENT_FRAMERATE_NEVER = JavaStaticField("I")
    MATCH_CONTENT_FRAMERATE_SEAMLESSS_ONLY = JavaStaticField("I")
    MATCH_CONTENT_FRAMERATE_UNKNOWN = JavaStaticField("I")
    VIRTUAL_DISPLAY_FLAG_AUTO_MIRROR = JavaStaticField("I")
    VIRTUAL_DISPLAY_FLAG_OWN_CONTENT_ONLY = JavaStaticField("I")
    VIRTUAL_DISPLAY_FLAG_PRESENTATION = JavaStaticField("I")
    VIRTUAL_DISPLAY_FLAG_PUBLIC = JavaStaticField("I")
    VIRTUAL_DISPLAY_FLAG_SECURE = JavaStaticField("I")
    getDisplay = JavaMethod("(I)Landroid/view/Display;")
    getDisplays = JavaMultipleMethod([("()[Landroid/view/Display;", False, False), ("(Ljava/lang/String;)[Landroid/view/Display;", False, False)])
    registerDisplayListener = JavaMethod("(Landroid/hardware/display/DisplayManager$DisplayListener;Landroid/os/Handler;)V")
    unregisterDisplayListener = JavaMethod("(Landroid/hardware/display/DisplayManager$DisplayListener;)V")
    createVirtualDisplay = JavaMultipleMethod([("(Ljava/lang/String;IIILandroid/view/Surface;I)Landroid/hardware/display/VirtualDisplay;", False, False), ("(Ljava/lang/String;IIILandroid/view/Surface;ILandroid/hardware/display/VirtualDisplay$Callback;Landroid/os/Handler;)Landroid/hardware/display/VirtualDisplay;", False, False), ("(Landroid/hardware/display/VirtualDisplayConfig;)Landroid/hardware/display/VirtualDisplay;", False, False), ("(Landroid/hardware/display/VirtualDisplayConfig;Landroid/os/Handler;Landroid/hardware/display/VirtualDisplay$Callback;)Landroid/hardware/display/VirtualDisplay;", False, False)])
    getHdrConversionMode = JavaMethod("()Landroid/hardware/display/HdrConversionMode;")
    getMatchContentFrameRateUserPreference = JavaMethod("()I")

    class DisplayListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/display/DisplayManager/DisplayListener"
        onDisplayAdded = JavaMethod("(I)V")
        onDisplayRemoved = JavaMethod("(I)V")
        onDisplayChanged = JavaMethod("(I)V")