from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Spatializer"]

class Spatializer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/Spatializer"
    SPATIALIZER_IMMERSIVE_LEVEL_MULTICHANNEL = JavaStaticField("I")
    SPATIALIZER_IMMERSIVE_LEVEL_NONE = JavaStaticField("I")
    SPATIALIZER_IMMERSIVE_LEVEL_OTHER = JavaStaticField("I")
    isAvailable = JavaMethod("()Z")
    canBeSpatialized = JavaMethod("(Landroid/media/AudioAttributes;Landroid/media/AudioFormat;)Z")
    addOnHeadTrackerAvailableListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/Spatializer$OnHeadTrackerAvailableListener;)V")
    addOnSpatializerStateChangedListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/Spatializer$OnSpatializerStateChangedListener;)V")
    getImmersiveAudioLevel = JavaMethod("()I")
    getSpatializedChannelMasks = JavaMethod("()Ljava/util/List;")
    isHeadTrackerAvailable = JavaMethod("()Z")
    removeOnHeadTrackerAvailableListener = JavaMethod("(Landroid/media/Spatializer$OnHeadTrackerAvailableListener;)V")
    removeOnSpatializerStateChangedListener = JavaMethod("(Landroid/media/Spatializer$OnSpatializerStateChangedListener;)V")
    isEnabled = JavaMethod("()Z")

    class OnSpatializerStateChangedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/Spatializer$OnSpatializerStateChangedListener"
        onSpatializerAvailableChanged = JavaMethod("(Landroid/media/Spatializer;Z)V")
        onSpatializerEnabledChanged = JavaMethod("(Landroid/media/Spatializer;Z)V")

    class OnHeadTrackerAvailableListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/Spatializer$OnHeadTrackerAvailableListener"
        onHeadTrackerAvailableChanged = JavaMethod("(Landroid/media/Spatializer;Z)V")