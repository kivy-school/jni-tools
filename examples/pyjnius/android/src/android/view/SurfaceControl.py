from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SurfaceControl"]

class SurfaceControl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/SurfaceControl"
    BUFFER_TRANSFORM_IDENTITY = JavaStaticField("I")
    BUFFER_TRANSFORM_MIRROR_HORIZONTAL = JavaStaticField("I")
    BUFFER_TRANSFORM_MIRROR_VERTICAL = JavaStaticField("I")
    BUFFER_TRANSFORM_ROTATE_180 = JavaStaticField("I")
    BUFFER_TRANSFORM_ROTATE_270 = JavaStaticField("I")
    BUFFER_TRANSFORM_ROTATE_90 = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    release = JavaMethod("()V")
    isValid = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    readFromParcel = JavaMethod("(Landroid/os/Parcel;)V")
    describeContents = JavaMethod("()I")

    class TrustedPresentationThresholds(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControl$TrustedPresentationThresholds"
        __javaconstructor__ = [("(FFI)V", False)]

    class TransactionStats(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControl$TransactionStats"
        getPresentFence = JavaMethod("()Landroid/hardware/SyncFence;")
        getLatchTimeNanos = JavaMethod("()J")

    class TransactionCommittedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControl$TransactionCommittedListener"
        onTransactionCommitted = JavaMethod("()V")

    class Transaction(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControl$Transaction"
        __javaconstructor__ = [("()V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        apply = JavaMethod("()V")
        merge = JavaMethod("(Landroid/view/SurfaceControl$Transaction;)Landroid/view/SurfaceControl$Transaction;")
        close = JavaMethod("()V")
        setOpaque = JavaMethod("(Landroid/view/SurfaceControl;Z)Landroid/view/SurfaceControl$Transaction;")
        setBufferSize = JavaMethod("(Landroid/view/SurfaceControl;II)Landroid/view/SurfaceControl$Transaction;")
        setCrop = JavaMethod("(Landroid/view/SurfaceControl;Landroid/graphics/Rect;)Landroid/view/SurfaceControl$Transaction;")
        setBufferTransform = JavaMethod("(Landroid/view/SurfaceControl;I)Landroid/view/SurfaceControl$Transaction;")
        setBuffer = JavaMultipleMethod([("(Landroid/view/SurfaceControl;Landroid/hardware/HardwareBuffer;)Landroid/view/SurfaceControl$Transaction;", False, False), ("(Landroid/view/SurfaceControl;Landroid/hardware/HardwareBuffer;Landroid/hardware/SyncFence;)Landroid/view/SurfaceControl$Transaction;", False, False), ("(Landroid/view/SurfaceControl;Landroid/hardware/HardwareBuffer;Landroid/hardware/SyncFence;Ljava/util/function/Consumer;)Landroid/view/SurfaceControl$Transaction;", False, False)])
        addTransactionCompletedListener = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)Landroid/view/SurfaceControl$Transaction;")
        reparent = JavaMethod("(Landroid/view/SurfaceControl;Landroid/view/SurfaceControl;)Landroid/view/SurfaceControl$Transaction;")
        setContentPriority = JavaMethod("(Landroid/view/SurfaceControl;I)Landroid/view/SurfaceControl$Transaction;")
        addTransactionCommittedListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/view/SurfaceControl$TransactionCommittedListener;)Landroid/view/SurfaceControl$Transaction;")
        clearTrustedPresentationCallback = JavaMethod("(Landroid/view/SurfaceControl;)Landroid/view/SurfaceControl$Transaction;")
        setDamageRegion = JavaMethod("(Landroid/view/SurfaceControl;Landroid/graphics/Region;)Landroid/view/SurfaceControl$Transaction;")
        setDesiredPresentTimeNanos = JavaMethod("(J)Landroid/view/SurfaceControl$Transaction;")
        setExtendedRangeBrightness = JavaMethod("(Landroid/view/SurfaceControl;FF)Landroid/view/SurfaceControl$Transaction;")
        setFrameTimeline = JavaMethod("(J)Landroid/view/SurfaceControl$Transaction;")
        setGeometry = JavaMethod("(Landroid/view/SurfaceControl;Landroid/graphics/Rect;Landroid/graphics/Rect;I)Landroid/view/SurfaceControl$Transaction;")
        setLayer = JavaMethod("(Landroid/view/SurfaceControl;I)Landroid/view/SurfaceControl$Transaction;")
        setLuts = JavaMethod("(Landroid/view/SurfaceControl;Landroid/hardware/DisplayLuts;)Landroid/view/SurfaceControl$Transaction;")
        setPosition = JavaMethod("(Landroid/view/SurfaceControl;FF)Landroid/view/SurfaceControl$Transaction;")
        setTrustedPresentationCallback = JavaMethod("(Landroid/view/SurfaceControl;Landroid/view/SurfaceControl$TrustedPresentationThresholds;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)Landroid/view/SurfaceControl$Transaction;")
        setDataSpace = JavaMethod("(Landroid/view/SurfaceControl;I)Landroid/view/SurfaceControl$Transaction;")
        setAlpha = JavaMethod("(Landroid/view/SurfaceControl;F)Landroid/view/SurfaceControl$Transaction;")
        setVisibility = JavaMethod("(Landroid/view/SurfaceControl;Z)Landroid/view/SurfaceControl$Transaction;")
        setScale = JavaMethod("(Landroid/view/SurfaceControl;FF)Landroid/view/SurfaceControl$Transaction;")
        clearFrameRate = JavaMethod("(Landroid/view/SurfaceControl;)Landroid/view/SurfaceControl$Transaction;")
        setFrameRate = JavaMultipleMethod([("(Landroid/view/SurfaceControl;FII)Landroid/view/SurfaceControl$Transaction;", False, False), ("(Landroid/view/SurfaceControl;FI)Landroid/view/SurfaceControl$Transaction;", False, False)])
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        setDesiredHdrHeadroom = JavaMethod("(Landroid/view/SurfaceControl;F)Landroid/view/SurfaceControl$Transaction;")

    class OnJankDataListenerRegistration(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControl$OnJankDataListenerRegistration"
        flush = JavaMethod("()V")
        removeAfter = JavaMethod("(J)V")

    class OnJankDataListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControl$OnJankDataListener"
        onJankDataAvailable = JavaMethod("(Ljava/util/List;)V")

    class JankData(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControl$JankData"
        JANK_APPLICATION = JavaStaticField("I")
        JANK_COMPOSER = JavaStaticField("I")
        JANK_NONE = JavaStaticField("I")
        JANK_OTHER = JavaStaticField("I")
        getVsyncId = JavaMethod("()J")
        toString = JavaMethod("()Ljava/lang/String;")
        getActualAppFrameTimeNanos = JavaMethod("()J")
        getJankType = JavaMethod("()I")
        getScheduledAppFrameTimeNanos = JavaMethod("()J")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControl$Builder"
        __javaconstructor__ = [("()V", False)]
        setName = JavaMethod("(Ljava/lang/String;)Landroid/view/SurfaceControl$Builder;")
        setOpaque = JavaMethod("(Z)Landroid/view/SurfaceControl$Builder;")
        setBufferSize = JavaMethod("(II)Landroid/view/SurfaceControl$Builder;")
        setHidden = JavaMethod("(Z)Landroid/view/SurfaceControl$Builder;")
        setParent = JavaMethod("(Landroid/view/SurfaceControl;)Landroid/view/SurfaceControl$Builder;")
        build = JavaMethod("()Landroid/view/SurfaceControl;")
        setFormat = JavaMethod("(I)Landroid/view/SurfaceControl$Builder;")