from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioMetadataMap"]

class AudioMetadataMap(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioMetadataMap"
    remove = JavaMethod("(Landroid/media/AudioMetadata$Key;)Ljava/lang/Object;")
    set = JavaMethod("(Landroid/media/AudioMetadata$Key;Ljava/lang/Object;)Ljava/lang/Object;")