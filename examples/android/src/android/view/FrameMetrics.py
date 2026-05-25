from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FrameMetrics"]

class FrameMetrics(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/FrameMetrics"
    __javaconstructor__ = [("(Landroid/view/FrameMetrics;)V", False)]
    ANIMATION_DURATION = JavaStaticField("I")
    COMMAND_ISSUE_DURATION = JavaStaticField("I")
    DEADLINE = JavaStaticField("I")
    DRAW_DURATION = JavaStaticField("I")
    FIRST_DRAW_FRAME = JavaStaticField("I")
    GPU_DURATION = JavaStaticField("I")
    INPUT_HANDLING_DURATION = JavaStaticField("I")
    INTENDED_VSYNC_TIMESTAMP = JavaStaticField("I")
    LAYOUT_MEASURE_DURATION = JavaStaticField("I")
    SWAP_BUFFERS_DURATION = JavaStaticField("I")
    SYNC_DURATION = JavaStaticField("I")
    TOTAL_DURATION = JavaStaticField("I")
    UNKNOWN_DELAY_DURATION = JavaStaticField("I")
    VSYNC_TIMESTAMP = JavaStaticField("I")
    getMetric = JavaMethod("(I)J")