from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioMetadataMap"]

class AudioMetadataMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioMetadataMap"
    remove = JavaMethod("(Landroid/media/AudioMetadata$Key;)Ljava/lang/Object;")
    set = JavaMethod("(Landroid/media/AudioMetadata$Key;Ljava/lang/Object;)Ljava/lang/Object;")