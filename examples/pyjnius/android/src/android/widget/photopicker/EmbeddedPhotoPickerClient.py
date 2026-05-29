from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EmbeddedPhotoPickerClient"]

class EmbeddedPhotoPickerClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/photopicker/EmbeddedPhotoPickerClient"
    onSessionOpened = JavaMethod("(Landroid/widget/photopicker/EmbeddedPhotoPickerSession;)V")
    onSessionError = JavaMethod("(Ljava/lang/Throwable;)V")
    onUriPermissionGranted = JavaMethod("(Ljava/util/List;)V")
    onUriPermissionRevoked = JavaMethod("(Ljava/util/List;)V")
    onSelectionComplete = JavaMethod("()V")