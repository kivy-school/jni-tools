from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Visualizer"]

class Visualizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/audiofx/Visualizer"
    __javaconstructor__ = [("(I)V", False)]
    ALREADY_EXISTS = JavaStaticField("I")
    ERROR = JavaStaticField("I")
    ERROR_BAD_VALUE = JavaStaticField("I")
    ERROR_DEAD_OBJECT = JavaStaticField("I")
    ERROR_INVALID_OPERATION = JavaStaticField("I")
    ERROR_NO_INIT = JavaStaticField("I")
    ERROR_NO_MEMORY = JavaStaticField("I")
    MEASUREMENT_MODE_NONE = JavaStaticField("I")
    MEASUREMENT_MODE_PEAK_RMS = JavaStaticField("I")
    SCALING_MODE_AS_PLAYED = JavaStaticField("I")
    SCALING_MODE_NORMALIZED = JavaStaticField("I")
    STATE_ENABLED = JavaStaticField("I")
    STATE_INITIALIZED = JavaStaticField("I")
    STATE_UNINITIALIZED = JavaStaticField("I")
    SUCCESS = JavaStaticField("I")
    release = JavaMethod("()V")
    finalize = JavaMethod("()V")
    setEnabled = JavaMethod("(Z)I")
    getEnabled = JavaMethod("()Z")
    getCaptureSizeRange = JavaStaticMethod("()[I")
    getMaxCaptureRate = JavaStaticMethod("()I")
    setCaptureSize = JavaMethod("(I)I")
    getCaptureSize = JavaMethod("()I")
    setScalingMode = JavaMethod("(I)I")
    getScalingMode = JavaMethod("()I")
    setMeasurementMode = JavaMethod("(I)I")
    getMeasurementMode = JavaMethod("()I")
    getSamplingRate = JavaMethod("()I")
    getWaveForm = JavaMethod("([B)I")
    getFft = JavaMethod("([B)I")
    getMeasurementPeakRms = JavaMethod("(Landroid/media/audiofx/Visualizer$MeasurementPeakRms;)I")
    setDataCaptureListener = JavaMethod("(Landroid/media/audiofx/Visualizer$OnDataCaptureListener;IZZ)I")

    class MeasurementPeakRms(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/Visualizer/MeasurementPeakRms"
        __javaconstructor__ = [("()V", False)]
        mPeak = JavaField("I")
        mRms = JavaField("I")

    class OnDataCaptureListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/Visualizer/OnDataCaptureListener"
        onWaveFormDataCapture = JavaMethod("(Landroid/media/audiofx/Visualizer;[BI)V")
        onFftDataCapture = JavaMethod("(Landroid/media/audiofx/Visualizer;[BI)V")