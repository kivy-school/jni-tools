from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaPlayer"]

class MediaPlayer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaPlayer"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;)V", False)]
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
    setDisplay = JavaMethod("(Landroid/view/SurfaceHolder;)V")
    setSurface = JavaMethod("(Landroid/view/Surface;)V")
    setVideoScalingMode = JavaMethod("(I)V")
    create = JavaMultipleMethod([("(Landroid/content/Context;Landroid/net/Uri;)Landroid/media/MediaPlayer;", True, False), ("(Landroid/content/Context;Landroid/net/Uri;Landroid/view/SurfaceHolder;)Landroid/media/MediaPlayer;", True, False), ("(Landroid/content/Context;Landroid/net/Uri;Landroid/view/SurfaceHolder;Landroid/media/AudioAttributes;I)Landroid/media/MediaPlayer;", True, False), ("(Landroid/content/Context;I)Landroid/media/MediaPlayer;", True, False), ("(Landroid/content/Context;ILandroid/media/AudioAttributes;I)Landroid/media/MediaPlayer;", True, False)])
    setDataSource = JavaMultipleMethod([("(Landroid/content/Context;Landroid/net/Uri;)V", False, False), ("(Landroid/content/Context;Landroid/net/Uri;Ljava/util/Map;Ljava/util/List;)V", False, False), ("(Landroid/content/Context;Landroid/net/Uri;Ljava/util/Map;)V", False, False), ("(Ljava/lang/String;)V", False, False), ("(Landroid/content/res/AssetFileDescriptor;)V", False, False), ("(Ljava/io/FileDescriptor;)V", False, False), ("(Ljava/io/FileDescriptor;JJ)V", False, False), ("(Landroid/media/MediaDataSource;)V", False, False)])
    prepare = JavaMethod("()V")
    prepareAsync = JavaMethod("()V")
    start = JavaMethod("()V")
    stop = JavaMethod("()V")
    pause = JavaMethod("()V")
    createVolumeShaper = JavaMethod("(Landroid/media/VolumeShaper$Configuration;)Landroid/media/VolumeShaper;")
    setPreferredDevice = JavaMethod("(Landroid/media/AudioDeviceInfo;)Z")
    getPreferredDevice = JavaMethod("()Landroid/media/AudioDeviceInfo;")
    getRoutedDevice = JavaMethod("()Landroid/media/AudioDeviceInfo;")
    addOnRoutingChangedListener = JavaMethod("(Landroid/media/AudioRouting$OnRoutingChangedListener;Landroid/os/Handler;)V")
    removeOnRoutingChangedListener = JavaMethod("(Landroid/media/AudioRouting$OnRoutingChangedListener;)V")
    setWakeMode = JavaMethod("(Landroid/content/Context;I)V")
    setScreenOnWhilePlaying = JavaMethod("(Z)V")
    getVideoWidth = JavaMethod("()I")
    getVideoHeight = JavaMethod("()I")
    getMetrics = JavaMethod("()Landroid/os/PersistableBundle;")
    isPlaying = JavaMethod("()Z")
    setPlaybackParams = JavaMethod("(Landroid/media/PlaybackParams;)V")
    getPlaybackParams = JavaMethod("()Landroid/media/PlaybackParams;")
    setSyncParams = JavaMethod("(Landroid/media/SyncParams;)V")
    getSyncParams = JavaMethod("()Landroid/media/SyncParams;")
    seekTo = JavaMultipleMethod([("(JI)V", False, False), ("(I)V", False, False)])
    getTimestamp = JavaMethod("()Landroid/media/MediaTimestamp;")
    getCurrentPosition = JavaMethod("()I")
    getDuration = JavaMethod("()I")
    setNextMediaPlayer = JavaMethod("(Landroid/media/MediaPlayer;)V")
    release = JavaMethod("()V")
    reset = JavaMethod("()V")
    setAudioStreamType = JavaMethod("(I)V")
    setAudioAttributes = JavaMethod("(Landroid/media/AudioAttributes;)V")
    setLooping = JavaMethod("(Z)V")
    isLooping = JavaMethod("()Z")
    setVolume = JavaMethod("(FF)V")
    setAudioSessionId = JavaMethod("(I)V")
    getAudioSessionId = JavaMethod("()I")
    attachAuxEffect = JavaMethod("(I)V")
    setAuxEffectSendLevel = JavaMethod("(F)V")
    getTrackInfo = JavaMethod("()[Landroid/media/MediaPlayer$TrackInfo;")
    addTimedTextSource = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)V", False, False), ("(Landroid/content/Context;Landroid/net/Uri;Ljava/lang/String;)V", False, False), ("(Ljava/io/FileDescriptor;Ljava/lang/String;)V", False, False), ("(Ljava/io/FileDescriptor;JJLjava/lang/String;)V", False, False)])
    getSelectedTrack = JavaMethod("(I)I")
    selectTrack = JavaMethod("(I)V")
    deselectTrack = JavaMethod("(I)V")
    finalize = JavaMethod("()V")
    setOnPreparedListener = JavaMethod("(Landroid/media/MediaPlayer$OnPreparedListener;)V")
    setOnCompletionListener = JavaMethod("(Landroid/media/MediaPlayer$OnCompletionListener;)V")
    setOnBufferingUpdateListener = JavaMethod("(Landroid/media/MediaPlayer$OnBufferingUpdateListener;)V")
    setOnSeekCompleteListener = JavaMethod("(Landroid/media/MediaPlayer$OnSeekCompleteListener;)V")
    setOnVideoSizeChangedListener = JavaMethod("(Landroid/media/MediaPlayer$OnVideoSizeChangedListener;)V")
    setOnTimedTextListener = JavaMethod("(Landroid/media/MediaPlayer$OnTimedTextListener;)V")
    setOnSubtitleDataListener = JavaMultipleMethod([("(Landroid/media/MediaPlayer$OnSubtitleDataListener;Landroid/os/Handler;)V", False, False), ("(Landroid/media/MediaPlayer$OnSubtitleDataListener;)V", False, False)])
    clearOnSubtitleDataListener = JavaMethod("()V")
    setOnMediaTimeDiscontinuityListener = JavaMultipleMethod([("(Landroid/media/MediaPlayer$OnMediaTimeDiscontinuityListener;Landroid/os/Handler;)V", False, False), ("(Landroid/media/MediaPlayer$OnMediaTimeDiscontinuityListener;)V", False, False)])
    clearOnMediaTimeDiscontinuityListener = JavaMethod("()V")
    setOnTimedMetaDataAvailableListener = JavaMethod("(Landroid/media/MediaPlayer$OnTimedMetaDataAvailableListener;)V")
    setOnErrorListener = JavaMethod("(Landroid/media/MediaPlayer$OnErrorListener;)V")
    setOnInfoListener = JavaMethod("(Landroid/media/MediaPlayer$OnInfoListener;)V")
    setOnDrmConfigHelper = JavaMethod("(Landroid/media/MediaPlayer$OnDrmConfigHelper;)V")
    setOnDrmInfoListener = JavaMultipleMethod([("(Landroid/media/MediaPlayer$OnDrmInfoListener;)V", False, False), ("(Landroid/media/MediaPlayer$OnDrmInfoListener;Landroid/os/Handler;)V", False, False)])
    setOnDrmPreparedListener = JavaMultipleMethod([("(Landroid/media/MediaPlayer$OnDrmPreparedListener;)V", False, False), ("(Landroid/media/MediaPlayer$OnDrmPreparedListener;Landroid/os/Handler;)V", False, False)])
    getDrmInfo = JavaMethod("()Landroid/media/MediaPlayer$DrmInfo;")
    prepareDrm = JavaMethod("(Ljava/util/UUID;)V")
    releaseDrm = JavaMethod("()V")
    getKeyRequest = JavaMethod("([B[BLjava/lang/String;ILjava/util/Map;)Landroid/media/MediaDrm$KeyRequest;")
    provideKeyResponse = JavaMethod("([B[B)[B")
    restoreKeys = JavaMethod("([B)V")
    getDrmPropertyString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    setDrmPropertyString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")

    class DrmInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/DrmInfo"
        getPssh = JavaMethod("()Ljava/util/Map;")
        getSupportedSchemes = JavaMethod("()[Ljava/util/UUID;")

    class MetricsConstants(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/MetricsConstants"
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

    class NoDrmSchemeException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/NoDrmSchemeException"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]

    class OnBufferingUpdateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnBufferingUpdateListener"
        onBufferingUpdate = JavaMethod("(Landroid/media/MediaPlayer;I)V")

    class OnCompletionListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnCompletionListener"
        onCompletion = JavaMethod("(Landroid/media/MediaPlayer;)V")

    class OnDrmConfigHelper(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnDrmConfigHelper"
        onDrmConfig = JavaMethod("(Landroid/media/MediaPlayer;)V")

    class OnDrmInfoListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnDrmInfoListener"
        onDrmInfo = JavaMethod("(Landroid/media/MediaPlayer;Landroid/media/MediaPlayer$DrmInfo;)V")

    class OnDrmPreparedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnDrmPreparedListener"
        onDrmPrepared = JavaMethod("(Landroid/media/MediaPlayer;I)V")

    class OnErrorListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnErrorListener"
        onError = JavaMethod("(Landroid/media/MediaPlayer;II)Z")

    class OnInfoListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnInfoListener"
        onInfo = JavaMethod("(Landroid/media/MediaPlayer;II)Z")

    class OnMediaTimeDiscontinuityListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnMediaTimeDiscontinuityListener"
        onMediaTimeDiscontinuity = JavaMethod("(Landroid/media/MediaPlayer;Landroid/media/MediaTimestamp;)V")

    class OnPreparedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnPreparedListener"
        onPrepared = JavaMethod("(Landroid/media/MediaPlayer;)V")

    class OnSeekCompleteListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnSeekCompleteListener"
        onSeekComplete = JavaMethod("(Landroid/media/MediaPlayer;)V")

    class OnSubtitleDataListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnSubtitleDataListener"
        onSubtitleData = JavaMethod("(Landroid/media/MediaPlayer;Landroid/media/SubtitleData;)V")

    class OnTimedMetaDataAvailableListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnTimedMetaDataAvailableListener"
        onTimedMetaDataAvailable = JavaMethod("(Landroid/media/MediaPlayer;Landroid/media/TimedMetaData;)V")

    class OnTimedTextListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnTimedTextListener"
        onTimedText = JavaMethod("(Landroid/media/MediaPlayer;Landroid/media/TimedText;)V")

    class OnVideoSizeChangedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/OnVideoSizeChangedListener"
        onVideoSizeChanged = JavaMethod("(Landroid/media/MediaPlayer;II)V")

    class ProvisioningNetworkErrorException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/ProvisioningNetworkErrorException"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]

    class ProvisioningServerErrorException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/ProvisioningServerErrorException"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]

    class TrackInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaPlayer/TrackInfo"
        MEDIA_TRACK_TYPE_AUDIO = JavaStaticField("I")
        MEDIA_TRACK_TYPE_METADATA = JavaStaticField("I")
        MEDIA_TRACK_TYPE_SUBTITLE = JavaStaticField("I")
        MEDIA_TRACK_TYPE_TIMEDTEXT = JavaStaticField("I")
        MEDIA_TRACK_TYPE_UNKNOWN = JavaStaticField("I")
        MEDIA_TRACK_TYPE_VIDEO = JavaStaticField("I")
        getTrackType = JavaMethod("()I")
        getLanguage = JavaMethod("()Ljava/lang/String;")
        getFormat = JavaMethod("()Landroid/media/MediaFormat;")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        toString = JavaMethod("()Ljava/lang/String;")