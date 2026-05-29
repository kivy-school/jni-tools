from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PermissionRequest"]

class PermissionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/PermissionRequest"
    __javaconstructor__ = [("()V", False)]
    RESOURCE_AUDIO_CAPTURE = JavaStaticField("Ljava/lang/String;")
    RESOURCE_MIDI_SYSEX = JavaStaticField("Ljava/lang/String;")
    RESOURCE_PROTECTED_MEDIA_ID = JavaStaticField("Ljava/lang/String;")
    RESOURCE_VIDEO_CAPTURE = JavaStaticField("Ljava/lang/String;")
    getOrigin = JavaMethod("()Landroid/net/Uri;")
    getResources = JavaMethod("()[Ljava/lang/String;")
    grant = JavaMethod("([Ljava/lang/String;)V")
    deny = JavaMethod("()V")