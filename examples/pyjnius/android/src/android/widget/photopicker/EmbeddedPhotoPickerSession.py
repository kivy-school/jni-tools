from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EmbeddedPhotoPickerSession"]

class EmbeddedPhotoPickerSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/photopicker/EmbeddedPhotoPickerSession"
    close = JavaMethod("()V")
    getSurfacePackage = JavaMethod("()Landroid/view/SurfaceControlViewHost$SurfacePackage;")
    notifyConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    notifyResized = JavaMethod("(II)V")
    notifyPhotoPickerExpanded = JavaMethod("(Z)V")
    notifyVisibilityChanged = JavaMethod("(Z)V")
    requestRevokeUriPermission = JavaMethod("(Ljava/util/List;)V")