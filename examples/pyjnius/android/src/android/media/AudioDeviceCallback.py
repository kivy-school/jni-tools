from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioDeviceCallback"]

class AudioDeviceCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioDeviceCallback"
    __javaconstructor__ = [("()V", False)]
    onAudioDevicesAdded = JavaMethod("([Landroid/media/AudioDeviceInfo;)V")
    onAudioDevicesRemoved = JavaMethod("([Landroid/media/AudioDeviceInfo;)V")