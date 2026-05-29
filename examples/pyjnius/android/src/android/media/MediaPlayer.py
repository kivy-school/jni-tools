from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaPlayer"]

class MediaPlayer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaPlayer"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("()V", False)]
    MEDIA_ERROR_IO = JavaStaticField("I")
    MEDIA_ERROR_MALFORMED = JavaStaticField("I")
    MEDIA_ERROR_NOT_VALID_FOR_PROGRESSIVE_PLAYBACK = JavaStaticField("I")
    MEDIA_ERROR_SERVER_DIED = JavaStaticField("I")
    MEDIA_ERROR_TIMED_OUT = JavaStaticField("I")
    MEDIA_ERROR_UNKNOWN = JavaStaticField("I")
    MEDIA_ERROR_UNSUPPORTED = JavaStaticField("I")
    MEDIA_INFO_AUDIO_NOT_PLAYING = JavaStaticField("I")
    MEDIA_INFO_BAD_INTERLEAVING = JavaStaticField("I")
    MEDIA_INFO_BUFFERING_END = JavaStaticField("I")
    MEDIA_INFO_BUFFERING_START = JavaStaticField("I")
    MEDIA_INFO_METADATA_UPDATE = JavaStaticField("I")
    MEDIA_INFO_NOT_SEEKABLE = JavaStaticField("I")
    MEDIA_INFO_STARTED_AS_NEXT = JavaStaticField("I")
    MEDIA_INFO_SUBTITLE_TIMED_OUT = JavaStaticField("I")
    MEDIA_INFO_UNKNOWN = JavaStaticField("I")
    MEDIA_INFO_UNSUPPORTED_SUBTITLE = JavaStaticField("I")
    MEDIA_INFO_VIDEO_NOT_PLAYING = JavaStaticField("I")
    MEDIA_INFO_VIDEO_RENDERING_START = JavaStaticField("I")
    MEDIA_INFO_VIDEO_TRACK_LAGGING = JavaStaticField("I")
    MEDIA_MIMETYPE_TEXT_SUBRIP = JavaStaticField("Ljava/lang/String;")
    PREPARE_DRM_STATUS_PREPARATION_ERROR = JavaStaticField("I")
    PREPARE_DRM_STATUS_PROVISIONING_NETWORK_ERROR = JavaStaticField("I")
    PREPARE_DRM_STATUS_PROVISIONING_SERVER_ERROR = JavaStaticField("I")
    PREPARE_DRM_STATUS_SUCCESS = JavaStaticField("I")
    SEEK_CLOSEST = JavaStaticField("I")
    SEEK_CLOSEST_SYNC = JavaStaticField("I")
    SEEK_NEXT_SYNC = JavaStaticField("I")
    SEEK_PREVIOUS_SYNC = JavaStaticField("I")
    VIDEO_SCALING_MODE_SCALE_TO_FIT = JavaStaticField("I")
    VIDEO_SCALING_MODE_SCALE_TO_FIT_WITH_CROPPING = JavaStaticField("I")
    getMetrics = JavaMethod("()Landroid/os/PersistableBundle;")
    isLooping = JavaMethod("()Z")
    setLooping = JavaMethod("(Z)V")
    setVolume = JavaMethod("(FF)V")
    addOnRoutingChangedListener = JavaMethod("(Landroid/media/AudioRouting$OnRoutingChangedListener;Landroid/os/Handler;)V")
    addTimedTextSource = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)V", False, False), ("(Ljava/io/FileDescriptor;JJLjava/lang/String;)V", False, False), ("(Ljava/io/FileDescriptor;Ljava/lang/String;)V", False, False), ("(Landroid/content/Context;Landroid/net/Uri;Ljava/lang/String;)V", False, False)])
    attachAuxEffect = JavaMethod("(I)V")
    clearOnMediaTimeDiscontinuityListener = JavaMethod("()V")
    clearOnSubtitleDataListener = JavaMethod("()V")
    createVolumeShaper = JavaMethod("(Landroid/media/VolumeShaper$Configuration;)Landroid/media/VolumeShaper;")
    deselectTrack = JavaMethod("(I)V")
    getDrmInfo = JavaMethod("()Landroid/media/MediaPlayer$DrmInfo;")
    getDrmPropertyString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getKeyRequest = JavaMethod("([B[BLjava/lang/String;ILjava/util/Map;)Landroid/media/MediaDrm$KeyRequest;")
    getPlaybackParams = JavaMethod("()Landroid/media/PlaybackParams;")
    getPreferredDevice = JavaMethod("()Landroid/media/AudioDeviceInfo;")
    getRoutedDevice = JavaMethod("()Landroid/media/AudioDeviceInfo;")
    getRoutedDevices = JavaMethod("()Ljava/util/List;")
    getSelectedTrack = JavaMethod("(I)I")
    getSyncParams = JavaMethod("()Landroid/media/SyncParams;")
    getTrackInfo = JavaMethod("()[Landroid/media/MediaPlayer$TrackInfo;")
    getVideoHeight = JavaMethod("()I")
    getVideoWidth = JavaMethod("()I")
    prepareAsync = JavaMethod("()V")
    prepareDrm = JavaMethod("(Ljava/util/UUID;)V")
    provideKeyResponse = JavaMethod("([B[B)[B")
    releaseDrm = JavaMethod("()V")
    removeOnRoutingChangedListener = JavaMethod("(Landroid/media/AudioRouting$OnRoutingChangedListener;)V")
    restoreKeys = JavaMethod("([B)V")
    selectTrack = JavaMethod("(I)V")
    setAudioSessionId = JavaMethod("(I)V")
    setAudioStreamType = JavaMethod("(I)V")
    setAuxEffectSendLevel = JavaMethod("(F)V")
    setDataSource = JavaMultipleMethod([("(Landroid/content/Context;Landroid/net/Uri;Ljava/util/Map;Ljava/util/List;)V", False, False), ("(Ljava/io/FileDescriptor;)V", False, False), ("(Landroid/content/res/AssetFileDescriptor;)V", False, False), ("(Landroid/media/MediaDataSource;)V", False, False), ("(Landroid/content/Context;Landroid/net/Uri;)V", False, False), ("(Landroid/content/Context;Landroid/net/Uri;Ljava/util/Map;)V", False, False), ("(Ljava/lang/String;)V", False, False), ("(Ljava/io/FileDescriptor;JJ)V", False, False)])
    setDisplay = JavaMethod("(Landroid/view/SurfaceHolder;)V")
    setDrmPropertyString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    setNextMediaPlayer = JavaMethod("(Landroid/media/MediaPlayer;)V")
    setOnBufferingUpdateListener = JavaMethod("(Landroid/media/MediaPlayer$OnBufferingUpdateListener;)V")
    setOnDrmConfigHelper = JavaMethod("(Landroid/media/MediaPlayer$OnDrmConfigHelper;)V")
    setOnDrmInfoListener = JavaMultipleMethod([("(Landroid/media/MediaPlayer$OnDrmInfoListener;Landroid/os/Handler;)V", False, False), ("(Landroid/media/MediaPlayer$OnDrmInfoListener;)V", False, False)])
    setOnDrmPreparedListener = JavaMultipleMethod([("(Landroid/media/MediaPlayer$OnDrmPreparedListener;)V", False, False), ("(Landroid/media/MediaPlayer$OnDrmPreparedListener;Landroid/os/Handler;)V", False, False)])
    setOnMediaTimeDiscontinuityListener = JavaMultipleMethod([("(Landroid/media/MediaPlayer$OnMediaTimeDiscontinuityListener;Landroid/os/Handler;)V", False, False), ("(Landroid/media/MediaPlayer$OnMediaTimeDiscontinuityListener;)V", False, False)])
    setOnSeekCompleteListener = JavaMethod("(Landroid/media/MediaPlayer$OnSeekCompleteListener;)V")
    setOnSubtitleDataListener = JavaMultipleMethod([("(Landroid/media/MediaPlayer$OnSubtitleDataListener;)V", False, False), ("(Landroid/media/MediaPlayer$OnSubtitleDataListener;Landroid/os/Handler;)V", False, False)])
    setOnTimedMetaDataAvailableListener = JavaMethod("(Landroid/media/MediaPlayer$OnTimedMetaDataAvailableListener;)V")
    setOnTimedTextListener = JavaMethod("(Landroid/media/MediaPlayer$OnTimedTextListener;)V")
    setOnVideoSizeChangedListener = JavaMethod("(Landroid/media/MediaPlayer$OnVideoSizeChangedListener;)V")
    setPlaybackParams = JavaMethod("(Landroid/media/PlaybackParams;)V")
    setPreferredDevice = JavaMethod("(Landroid/media/AudioDeviceInfo;)Z")
    setScreenOnWhilePlaying = JavaMethod("(Z)V")
    setSyncParams = JavaMethod("(Landroid/media/SyncParams;)V")
    setVideoScalingMode = JavaMethod("(I)V")
    setWakeMode = JavaMethod("(Landroid/content/Context;I)V")
    reset = JavaMethod("()V")
    start = JavaMethod("()V")
    create = JavaMultipleMethod([("(Landroid/content/Context;I)Landroid/media/MediaPlayer;", True, False), ("(Landroid/content/Context;ILandroid/media/AudioAttributes;I)Landroid/media/MediaPlayer;", True, False), ("(Landroid/content/Context;Landroid/net/Uri;)Landroid/media/MediaPlayer;", True, False), ("(Landroid/content/Context;Landroid/net/Uri;Landroid/view/SurfaceHolder;Landroid/media/AudioAttributes;I)Landroid/media/MediaPlayer;", True, False), ("(Landroid/content/Context;Landroid/net/Uri;Landroid/view/SurfaceHolder;)Landroid/media/MediaPlayer;", True, False)])
    prepare = JavaMethod("()V")
    release = JavaMethod("()V")
    setSurface = JavaMethod("(Landroid/view/Surface;)V")
    getAudioSessionId = JavaMethod("()I")
    getCurrentPosition = JavaMethod("()I")
    getDuration = JavaMethod("()I")
    isPlaying = JavaMethod("()Z")
    pause = JavaMethod("()V")
    seekTo = JavaMultipleMethod([("(I)V", False, False), ("(JI)V", False, False)])
    setOnCompletionListener = JavaMethod("(Landroid/media/MediaPlayer$OnCompletionListener;)V")
    setOnErrorListener = JavaMethod("(Landroid/media/MediaPlayer$OnErrorListener;)V")
    setOnInfoListener = JavaMethod("(Landroid/media/MediaPlayer$OnInfoListener;)V")
    setOnPreparedListener = JavaMethod("(Landroid/media/MediaPlayer$OnPreparedListener;)V")
    getTimestamp = JavaMethod("()Landroid/media/MediaTimestamp;")
    setAudioAttributes = JavaMethod("(Landroid/media/AudioAttributes;)V")
    stop = JavaMethod("()V")

    class TrackInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$TrackInfo"
        MEDIA_TRACK_TYPE_AUDIO = JavaStaticField("I")
        MEDIA_TRACK_TYPE_METADATA = JavaStaticField("I")
        MEDIA_TRACK_TYPE_SUBTITLE = JavaStaticField("I")
        MEDIA_TRACK_TYPE_TIMEDTEXT = JavaStaticField("I")
        MEDIA_TRACK_TYPE_UNKNOWN = JavaStaticField("I")
        MEDIA_TRACK_TYPE_VIDEO = JavaStaticField("I")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getTrackType = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")
        getLanguage = JavaMethod("()Ljava/lang/String;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getFormat = JavaMethod("()Landroid/media/MediaFormat;")

    class ProvisioningServerErrorException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$ProvisioningServerErrorException"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]

    class ProvisioningNetworkErrorException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$ProvisioningNetworkErrorException"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]

    class OnVideoSizeChangedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnVideoSizeChangedListener"
        onVideoSizeChanged = JavaMethod("(Landroid/media/MediaPlayer;II)V")

    class OnTimedTextListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnTimedTextListener"
        onTimedText = JavaMethod("(Landroid/media/MediaPlayer;Landroid/media/TimedText;)V")

    class OnTimedMetaDataAvailableListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnTimedMetaDataAvailableListener"
        onTimedMetaDataAvailable = JavaMethod("(Landroid/media/MediaPlayer;Landroid/media/TimedMetaData;)V")

    class OnSubtitleDataListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnSubtitleDataListener"
        onSubtitleData = JavaMethod("(Landroid/media/MediaPlayer;Landroid/media/SubtitleData;)V")

    class OnSeekCompleteListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnSeekCompleteListener"
        onSeekComplete = JavaMethod("(Landroid/media/MediaPlayer;)V")

    class OnPreparedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnPreparedListener"
        onPrepared = JavaMethod("(Landroid/media/MediaPlayer;)V")

    class OnMediaTimeDiscontinuityListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnMediaTimeDiscontinuityListener"
        onMediaTimeDiscontinuity = JavaMethod("(Landroid/media/MediaPlayer;Landroid/media/MediaTimestamp;)V")

    class OnInfoListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnInfoListener"
        onInfo = JavaMethod("(Landroid/media/MediaPlayer;II)Z")

    class OnErrorListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnErrorListener"
        onError = JavaMethod("(Landroid/media/MediaPlayer;II)Z")

    class OnDrmPreparedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnDrmPreparedListener"
        onDrmPrepared = JavaMethod("(Landroid/media/MediaPlayer;I)V")

    class OnDrmInfoListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnDrmInfoListener"
        onDrmInfo = JavaMethod("(Landroid/media/MediaPlayer;Landroid/media/MediaPlayer$DrmInfo;)V")

    class OnDrmConfigHelper(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnDrmConfigHelper"
        onDrmConfig = JavaMethod("(Landroid/media/MediaPlayer;)V")

    class OnCompletionListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnCompletionListener"
        onCompletion = JavaMethod("(Landroid/media/MediaPlayer;)V")

    class OnBufferingUpdateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$OnBufferingUpdateListener"
        onBufferingUpdate = JavaMethod("(Landroid/media/MediaPlayer;I)V")

    class NoDrmSchemeException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$NoDrmSchemeException"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]

    class MetricsConstants(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$MetricsConstants"
        CODEC_AUDIO = JavaStaticField("Ljava/lang/String;")
        CODEC_VIDEO = JavaStaticField("Ljava/lang/String;")
        DURATION = JavaStaticField("Ljava/lang/String;")
        ERRORS = JavaStaticField("Ljava/lang/String;")
        ERROR_CODE = JavaStaticField("Ljava/lang/String;")
        FRAMES = JavaStaticField("Ljava/lang/String;")
        FRAMES_DROPPED = JavaStaticField("Ljava/lang/String;")
        HEIGHT = JavaStaticField("Ljava/lang/String;")
        MIME_TYPE_AUDIO = JavaStaticField("Ljava/lang/String;")
        MIME_TYPE_VIDEO = JavaStaticField("Ljava/lang/String;")
        PLAYING = JavaStaticField("Ljava/lang/String;")
        WIDTH = JavaStaticField("Ljava/lang/String;")

    class DrmInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer$DrmInfo"
        getPssh = JavaMethod("()Ljava/util/Map;")
        getSupportedSchemes = JavaMethod("()[Ljava/util/UUID;")