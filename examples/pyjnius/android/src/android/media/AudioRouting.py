from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioRouting"]

class AudioRouting(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioRouting"
    setPreferredDevice = JavaMethod("(Landroid/media/AudioDeviceInfo;)Z")
    getPreferredDevice = JavaMethod("()Landroid/media/AudioDeviceInfo;")
    getRoutedDevice = JavaMethod("()Landroid/media/AudioDeviceInfo;")
    addOnRoutingChangedListener = JavaMethod("(Landroid/media/AudioRouting$OnRoutingChangedListener;Landroid/os/Handler;)V")
    removeOnRoutingChangedListener = JavaMethod("(Landroid/media/AudioRouting$OnRoutingChangedListener;)V")

    class OnRoutingChangedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/AudioRouting/OnRoutingChangedListener"
        onRoutingChanged = JavaMethod("(Landroid/media/AudioRouting;)V")