from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VolumeAutomation"]

class VolumeAutomation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/VolumeAutomation"
    createVolumeShaper = JavaMethod("(Landroid/media/VolumeShaper$Configuration;)Landroid/media/VolumeShaper;")