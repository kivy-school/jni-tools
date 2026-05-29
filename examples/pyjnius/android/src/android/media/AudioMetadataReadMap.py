from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioMetadataReadMap"]

class AudioMetadataReadMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioMetadataReadMap"
    size = JavaMethod("()I")
    get = JavaMethod("(Landroid/media/AudioMetadata$Key;)Ljava/lang/Object;")
    containsKey = JavaMethod("(Landroid/media/AudioMetadata$Key;)Z")
    dup = JavaMethod("()Landroid/media/AudioMetadataMap;")