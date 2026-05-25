from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    readFromParcel = JavaMethod("(Landroid/os/Parcel;)V")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    finalize = JavaMethod("()V")
    release = JavaMethod("()V")
    isValid = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControl/Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/view/SurfaceControl;")
        setName = JavaMethod("(Ljava/lang/String;)Landroid/view/SurfaceControl$Builder;")
        setBufferSize = JavaMethod("(II)Landroid/view/SurfaceControl$Builder;")
        setFormat = JavaMethod("(I)Landroid/view/SurfaceControl$Builder;")
        setOpaque = JavaMethod("(Z)Landroid/view/SurfaceControl$Builder;")
        setHidden = JavaMethod("(Z)Landroid/view/SurfaceControl$Builder;")
        setParent = JavaMethod("(Landroid/view/SurfaceControl;)Landroid/view/SurfaceControl$Builder;")

    class Transaction(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControl/Transaction"
        __javaconstructor__ = [("()V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        apply = JavaMethod("()V")
        close = JavaMethod("()V")
        setVisibility = JavaMethod("(Landroid/view/SurfaceControl;Z)Landroid/view/SurfaceControl$Transaction;")
        setPosition = JavaMethod("(Landroid/view/SurfaceControl;FF)Landroid/view/SurfaceControl$Transaction;")
        setScale = JavaMethod("(Landroid/view/SurfaceControl;FF)Landroid/view/SurfaceControl$Transaction;")
        setBufferSize = JavaMethod("(Landroid/view/SurfaceControl;II)Landroid/view/SurfaceControl$Transaction;")
        setLayer = JavaMethod("(Landroid/view/SurfaceControl;I)Landroid/view/SurfaceControl$Transaction;")
        setAlpha = JavaMethod("(Landroid/view/SurfaceControl;F)Landroid/view/SurfaceControl$Transaction;")
        setGeometry = JavaMethod("(Landroid/view/SurfaceControl;Landroid/graphics/Rect;Landroid/graphics/Rect;I)Landroid/view/SurfaceControl$Transaction;")
        setCrop = JavaMethod("(Landroid/view/SurfaceControl;Landroid/graphics/Rect;)Landroid/view/SurfaceControl$Transaction;")
        reparent = JavaMethod("(Landroid/view/SurfaceControl;Landroid/view/SurfaceControl;)Landroid/view/SurfaceControl$Transaction;")
        setOpaque = JavaMethod("(Landroid/view/SurfaceControl;Z)Landroid/view/SurfaceControl$Transaction;")
        setFrameRate = JavaMultipleMethod([("(Landroid/view/SurfaceControl;FI)Landroid/view/SurfaceControl$Transaction;", False, False), ("(Landroid/view/SurfaceControl;FII)Landroid/view/SurfaceControl$Transaction;", False, False)])
        clearFrameRate = JavaMethod("(Landroid/view/SurfaceControl;)Landroid/view/SurfaceControl$Transaction;")
        setBuffer = JavaMultipleMethod([("(Landroid/view/SurfaceControl;Landroid/hardware/HardwareBuffer;)Landroid/view/SurfaceControl$Transaction;", False, False), ("(Landroid/view/SurfaceControl;Landroid/hardware/HardwareBuffer;Landroid/hardware/SyncFence;)Landroid/view/SurfaceControl$Transaction;", False, False), ("(Landroid/view/SurfaceControl;Landroid/hardware/HardwareBuffer;Landroid/hardware/SyncFence;Ljava/util/function/Consumer;)Landroid/view/SurfaceControl$Transaction;", False, False)])
        setBufferTransform = JavaMethod("(Landroid/view/SurfaceControl;I)Landroid/view/SurfaceControl$Transaction;")
        setDamageRegion = JavaMethod("(Landroid/view/SurfaceControl;Landroid/graphics/Region;)Landroid/view/SurfaceControl$Transaction;")
        setDataSpace = JavaMethod("(Landroid/view/SurfaceControl;I)Landroid/view/SurfaceControl$Transaction;")
        setExtendedRangeBrightness = JavaMethod("(Landroid/view/SurfaceControl;FF)Landroid/view/SurfaceControl$Transaction;")
        setDesiredHdrHeadroom = JavaMethod("(Landroid/view/SurfaceControl;F)Landroid/view/SurfaceControl$Transaction;")
        merge = JavaMethod("(Landroid/view/SurfaceControl$Transaction;)Landroid/view/SurfaceControl$Transaction;")
        setFrameTimeline = JavaMethod("(J)Landroid/view/SurfaceControl$Transaction;")
        addTransactionCommittedListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/view/SurfaceControl$TransactionCommittedListener;)Landroid/view/SurfaceControl$Transaction;")
        addTransactionCompletedListener = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)Landroid/view/SurfaceControl$Transaction;")
        setTrustedPresentationCallback = JavaMethod("(Landroid/view/SurfaceControl;Landroid/view/SurfaceControl$TrustedPresentationThresholds;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)Landroid/view/SurfaceControl$Transaction;")
        clearTrustedPresentationCallback = JavaMethod("(Landroid/view/SurfaceControl;)Landroid/view/SurfaceControl$Transaction;")
        setDesiredPresentTimeNanos = JavaMethod("(J)Landroid/view/SurfaceControl$Transaction;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")

    class TransactionCommittedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControl/TransactionCommittedListener"
        onTransactionCommitted = JavaMethod("()V")

    class TransactionStats(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControl/TransactionStats"
        getLatchTimeNanos = JavaMethod("()J")
        getPresentFence = JavaMethod("()Landroid/hardware/SyncFence;")

    class TrustedPresentationThresholds(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceControl/TrustedPresentationThresholds"
        __javaconstructor__ = [("(FFI)V", False)]