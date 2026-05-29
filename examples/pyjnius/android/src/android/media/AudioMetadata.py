from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioMetadata"]

class AudioMetadata(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioMetadata"
    createMap = JavaStaticMethod("()Landroid/media/AudioMetadataMap;")

    class Format(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/AudioMetadata/Format"
        KEY_ATMOS_PRESENT = JavaStaticField("Landroid/media/AudioMetadata$Key;")
        KEY_AUDIO_ENCODING = JavaStaticField("Landroid/media/AudioMetadata$Key;")
        KEY_BIT_RATE = JavaStaticField("Landroid/media/AudioMetadata$Key;")
        KEY_BIT_WIDTH = JavaStaticField("Landroid/media/AudioMetadata$Key;")
        KEY_CHANNEL_MASK = JavaStaticField("Landroid/media/AudioMetadata$Key;")
        KEY_MIME = JavaStaticField("Landroid/media/AudioMetadata$Key;")
        KEY_PRESENTATION_CONTENT_CLASSIFIER = JavaStaticField("Landroid/media/AudioMetadata$Key;")
        KEY_PRESENTATION_ID = JavaStaticField("Landroid/media/AudioMetadata$Key;")
        KEY_PRESENTATION_LANGUAGE = JavaStaticField("Landroid/media/AudioMetadata$Key;")
        KEY_PROGRAM_ID = JavaStaticField("Landroid/media/AudioMetadata$Key;")
        KEY_SAMPLE_RATE = JavaStaticField("Landroid/media/AudioMetadata$Key;")

    class Key(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/AudioMetadata/Key"
        getName = JavaMethod("()Ljava/lang/String;")
        getValueClass = JavaMethod("()Ljava/lang/Class;")