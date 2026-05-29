from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaProjectionManager"]

class MediaProjectionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/projection/MediaProjectionManager"
    getMediaProjection = JavaMethod("(ILandroid/content/Intent;)Landroid/media/projection/MediaProjection;")
    createScreenCaptureIntent = JavaMultipleMethod([("(Landroid/media/projection/MediaProjectionConfig;)Landroid/content/Intent;", False, False), ("()Landroid/content/Intent;", False, False)])