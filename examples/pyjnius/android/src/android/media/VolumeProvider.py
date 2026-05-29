from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VolumeProvider"]

class VolumeProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/VolumeProvider"
    __javaconstructor__ = [("(IIILjava/lang/String;)V", False), ("(III)V", False)]
    VOLUME_CONTROL_ABSOLUTE = JavaStaticField("I")
    VOLUME_CONTROL_FIXED = JavaStaticField("I")
    VOLUME_CONTROL_RELATIVE = JavaStaticField("I")
    getVolumeControlId = JavaMethod("()Ljava/lang/String;")
    onAdjustVolume = JavaMethod("(I)V")
    onSetVolumeTo = JavaMethod("(I)V")
    setCurrentVolume = JavaMethod("(I)V")
    getCurrentVolume = JavaMethod("()I")
    getMaxVolume = JavaMethod("()I")
    getVolumeControl = JavaMethod("()I")