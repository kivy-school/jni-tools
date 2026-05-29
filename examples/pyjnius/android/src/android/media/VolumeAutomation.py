from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VolumeAutomation"]

class VolumeAutomation(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/VolumeAutomation"
    createVolumeShaper = JavaMethod("(Landroid/media/VolumeShaper$Configuration;)Landroid/media/VolumeShaper;")