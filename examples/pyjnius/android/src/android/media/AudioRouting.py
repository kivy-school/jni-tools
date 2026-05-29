from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioRouting"]

class AudioRouting(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioRouting"
    addOnRoutingChangedListener = JavaMethod("(Landroid/media/AudioRouting$OnRoutingChangedListener;Landroid/os/Handler;)V")
    getPreferredDevice = JavaMethod("()Landroid/media/AudioDeviceInfo;")
    getRoutedDevice = JavaMethod("()Landroid/media/AudioDeviceInfo;")
    getRoutedDevices = JavaMethod("()Ljava/util/List;")
    removeOnRoutingChangedListener = JavaMethod("(Landroid/media/AudioRouting$OnRoutingChangedListener;)V")
    setPreferredDevice = JavaMethod("(Landroid/media/AudioDeviceInfo;)Z")

    class OnRoutingChangedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/AudioRouting$OnRoutingChangedListener"
        onRoutingChanged = JavaMethod("(Landroid/media/AudioRouting;)V")