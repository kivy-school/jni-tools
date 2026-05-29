from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioMetadataReadMap"]

class AudioMetadataReadMap(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioMetadataReadMap"
    containsKey = JavaMethod("(Landroid/media/AudioMetadata$Key;)Z")
    dup = JavaMethod("()Landroid/media/AudioMetadataMap;")
    get = JavaMethod("(Landroid/media/AudioMetadata$Key;)Ljava/lang/Object;")
    size = JavaMethod("()I")