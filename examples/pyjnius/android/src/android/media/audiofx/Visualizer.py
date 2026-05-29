from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    getEnabled = JavaMethod("()Z")
    getCaptureSize = JavaMethod("()I")
    getCaptureSizeRange = JavaStaticMethod("()[I")
    getFft = JavaMethod("([B)I")
    getMaxCaptureRate = JavaStaticMethod("()I")
    getMeasurementMode = JavaMethod("()I")
    getMeasurementPeakRms = JavaMethod("(Landroid/media/audiofx/Visualizer$MeasurementPeakRms;)I")
    getSamplingRate = JavaMethod("()I")
    getScalingMode = JavaMethod("()I")
    getWaveForm = JavaMethod("([B)I")
    setCaptureSize = JavaMethod("(I)I")
    setDataCaptureListener = JavaMethod("(Landroid/media/audiofx/Visualizer$OnDataCaptureListener;IZZ)I")
    setMeasurementMode = JavaMethod("(I)I")
    setScalingMode = JavaMethod("(I)I")
    release = JavaMethod("()V")
    setEnabled = JavaMethod("(Z)I")

    class OnDataCaptureListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/Visualizer$OnDataCaptureListener"
        onFftDataCapture = JavaMethod("(Landroid/media/audiofx/Visualizer;[BI)V")
        onWaveFormDataCapture = JavaMethod("(Landroid/media/audiofx/Visualizer;[BI)V")

    class MeasurementPeakRms(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/Visualizer$MeasurementPeakRms"
        __javaconstructor__ = [("()V", False)]
        mPeak = JavaField("I")
        mRms = JavaField("I")