from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CloudMediaProviderContract"]

class CloudMediaProviderContract(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/CloudMediaProviderContract"
    EXTRA_ALBUM_ID = JavaStaticField("Ljava/lang/String;")
    EXTRA_LOOPING_PLAYBACK_ENABLED = JavaStaticField("Ljava/lang/String;")
    EXTRA_MEDIA_COLLECTION_ID = JavaStaticField("Ljava/lang/String;")
    EXTRA_PAGE_SIZE = JavaStaticField("Ljava/lang/String;")
    EXTRA_PAGE_TOKEN = JavaStaticField("Ljava/lang/String;")
    EXTRA_PREVIEW_THUMBNAIL = JavaStaticField("Ljava/lang/String;")
    EXTRA_SURFACE_CONTROLLER_AUDIO_MUTE_ENABLED = JavaStaticField("Ljava/lang/String;")
    EXTRA_SYNC_GENERATION = JavaStaticField("Ljava/lang/String;")
    MANAGE_CLOUD_MEDIA_PROVIDERS_PERMISSION = JavaStaticField("Ljava/lang/String;")
    PROVIDER_INTERFACE = JavaStaticField("Ljava/lang/String;")

    class AlbumColumns(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/CloudMediaProviderContract/AlbumColumns"
        DATE_TAKEN_MILLIS = JavaStaticField("Ljava/lang/String;")
        DISPLAY_NAME = JavaStaticField("Ljava/lang/String;")
        ID = JavaStaticField("Ljava/lang/String;")
        MEDIA_COUNT = JavaStaticField("Ljava/lang/String;")
        MEDIA_COVER_ID = JavaStaticField("Ljava/lang/String;")

    class MediaCollectionInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/CloudMediaProviderContract/MediaCollectionInfo"
        ACCOUNT_CONFIGURATION_INTENT = JavaStaticField("Ljava/lang/String;")
        ACCOUNT_NAME = JavaStaticField("Ljava/lang/String;")
        LAST_MEDIA_SYNC_GENERATION = JavaStaticField("Ljava/lang/String;")
        MEDIA_COLLECTION_ID = JavaStaticField("Ljava/lang/String;")

    class MediaColumns(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/CloudMediaProviderContract/MediaColumns"
        DATE_TAKEN_MILLIS = JavaStaticField("Ljava/lang/String;")
        DURATION_MILLIS = JavaStaticField("Ljava/lang/String;")
        HEIGHT = JavaStaticField("Ljava/lang/String;")
        ID = JavaStaticField("Ljava/lang/String;")
        IS_FAVORITE = JavaStaticField("Ljava/lang/String;")
        MEDIA_STORE_URI = JavaStaticField("Ljava/lang/String;")
        MIME_TYPE = JavaStaticField("Ljava/lang/String;")
        ORIENTATION = JavaStaticField("Ljava/lang/String;")
        SIZE_BYTES = JavaStaticField("Ljava/lang/String;")
        STANDARD_MIME_TYPE_EXTENSION = JavaStaticField("Ljava/lang/String;")
        STANDARD_MIME_TYPE_EXTENSION_ANIMATED_WEBP = JavaStaticField("I")
        STANDARD_MIME_TYPE_EXTENSION_GIF = JavaStaticField("I")
        STANDARD_MIME_TYPE_EXTENSION_MOTION_PHOTO = JavaStaticField("I")
        STANDARD_MIME_TYPE_EXTENSION_NONE = JavaStaticField("I")
        SYNC_GENERATION = JavaStaticField("Ljava/lang/String;")
        WIDTH = JavaStaticField("Ljava/lang/String;")