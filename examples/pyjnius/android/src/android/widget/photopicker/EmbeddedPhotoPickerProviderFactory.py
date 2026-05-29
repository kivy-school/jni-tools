from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EmbeddedPhotoPickerProviderFactory"]

class EmbeddedPhotoPickerProviderFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/photopicker/EmbeddedPhotoPickerProviderFactory"
    create = JavaStaticMethod("(Landroid/content/Context;)Landroid/widget/photopicker/EmbeddedPhotoPickerProvider;")