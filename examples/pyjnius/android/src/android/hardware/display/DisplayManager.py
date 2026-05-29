from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DisplayManager"]

class DisplayManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/display/DisplayManager"
    DISPLAY_CATEGORY_PRESENTATION = JavaStaticField("Ljava/lang/String;")
    EVENT_TYPE_DISPLAY_ADDED = JavaStaticField("J")
    EVENT_TYPE_DISPLAY_CHANGED = JavaStaticField("J")
    EVENT_TYPE_DISPLAY_REFRESH_RATE = JavaStaticField("J")
    EVENT_TYPE_DISPLAY_REMOVED = JavaStaticField("J")
    EVENT_TYPE_DISPLAY_STATE = JavaStaticField("J")
    MATCH_CONTENT_FRAMERATE_ALWAYS = JavaStaticField("I")
    MATCH_CONTENT_FRAMERATE_NEVER = JavaStaticField("I")
    MATCH_CONTENT_FRAMERATE_SEAMLESSS_ONLY = JavaStaticField("I")
    MATCH_CONTENT_FRAMERATE_UNKNOWN = JavaStaticField("I")
    VIRTUAL_DISPLAY_FLAG_AUTO_MIRROR = JavaStaticField("I")
    VIRTUAL_DISPLAY_FLAG_OWN_CONTENT_ONLY = JavaStaticField("I")
    VIRTUAL_DISPLAY_FLAG_PRESENTATION = JavaStaticField("I")
    VIRTUAL_DISPLAY_FLAG_PUBLIC = JavaStaticField("I")
    VIRTUAL_DISPLAY_FLAG_SECURE = JavaStaticField("I")
    createVirtualDisplay = JavaMultipleMethod([("(Ljava/lang/String;IIILandroid/view/Surface;I)Landroid/hardware/display/VirtualDisplay;", False, False), ("(Landroid/hardware/display/VirtualDisplayConfig;Landroid/os/Handler;Landroid/hardware/display/VirtualDisplay$Callback;)Landroid/hardware/display/VirtualDisplay;", False, False), ("(Landroid/hardware/display/VirtualDisplayConfig;)Landroid/hardware/display/VirtualDisplay;", False, False), ("(Ljava/lang/String;IIILandroid/view/Surface;ILandroid/hardware/display/VirtualDisplay$Callback;Landroid/os/Handler;)Landroid/hardware/display/VirtualDisplay;", False, False)])
    getHdrConversionMode = JavaMethod("()Landroid/hardware/display/HdrConversionMode;")
    getMatchContentFrameRateUserPreference = JavaMethod("()I")
    registerDisplayListener = JavaMultipleMethod([("(Ljava/util/concurrent/Executor;JLandroid/hardware/display/DisplayManager$DisplayListener;)V", False, False), ("(Landroid/hardware/display/DisplayManager$DisplayListener;Landroid/os/Handler;)V", False, False)])
    unregisterDisplayListener = JavaMethod("(Landroid/hardware/display/DisplayManager$DisplayListener;)V")
    getDisplays = JavaMultipleMethod([("()[Landroid/view/Display;", False, False), ("(Ljava/lang/String;)[Landroid/view/Display;", False, False)])
    getDisplay = JavaMethod("(I)Landroid/view/Display;")

    class DisplayListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/display/DisplayManager$DisplayListener"
        onDisplayChanged = JavaMethod("(I)V")
        onDisplayRemoved = JavaMethod("(I)V")
        onDisplayAdded = JavaMethod("(I)V")