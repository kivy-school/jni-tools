from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VolumeProvider"]

class VolumeProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/VolumeProvider"
    __javaconstructor__ = [("(III)V", False), ("(IIILjava/lang/String;)V", False)]
    VOLUME_CONTROL_ABSOLUTE = JavaStaticField("I")
    VOLUME_CONTROL_FIXED = JavaStaticField("I")
    VOLUME_CONTROL_RELATIVE = JavaStaticField("I")
    getVolumeControl = JavaMethod("()I")
    getMaxVolume = JavaMethod("()I")
    getCurrentVolume = JavaMethod("()I")
    setCurrentVolume = JavaMethod("(I)V")
    getVolumeControlId = JavaMethod("()Ljava/lang/String;")
    onSetVolumeTo = JavaMethod("(I)V")
    onAdjustVolume = JavaMethod("(I)V")