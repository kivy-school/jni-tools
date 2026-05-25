from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaProjectionManager"]

class MediaProjectionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/projection/MediaProjectionManager"
    createScreenCaptureIntent = JavaMultipleMethod([("()Landroid/content/Intent;", False, False), ("(Landroid/media/projection/MediaProjectionConfig;)Landroid/content/Intent;", False, False)])
    getMediaProjection = JavaMethod("(ILandroid/content/Intent;)Landroid/media/projection/MediaProjection;")