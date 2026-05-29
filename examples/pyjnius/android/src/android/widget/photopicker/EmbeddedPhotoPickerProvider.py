from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EmbeddedPhotoPickerProvider"]

class EmbeddedPhotoPickerProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/photopicker/EmbeddedPhotoPickerProvider"
    openSession = JavaMethod("(Landroid/os/IBinder;IIILandroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo;Ljava/util/concurrent/Executor;Landroid/widget/photopicker/EmbeddedPhotoPickerClient;)V")