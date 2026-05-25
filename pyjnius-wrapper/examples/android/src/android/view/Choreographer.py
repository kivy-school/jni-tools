from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Choreographer"]

class Choreographer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/Choreographer"
    getInstance = JavaStaticMethod("()Landroid/view/Choreographer;")
    postVsyncCallback = JavaMethod("(Landroid/view/Choreographer$VsyncCallback;)V")
    postFrameCallback = JavaMethod("(Landroid/view/Choreographer$FrameCallback;)V")
    postFrameCallbackDelayed = JavaMethod("(Landroid/view/Choreographer$FrameCallback;J)V")
    removeFrameCallback = JavaMethod("(Landroid/view/Choreographer$FrameCallback;)V")
    removeVsyncCallback = JavaMethod("(Landroid/view/Choreographer$VsyncCallback;)V")

    class FrameCallback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/Choreographer/FrameCallback"
        doFrame = JavaMethod("(J)V")

    class FrameData(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/Choreographer/FrameData"
        getFrameTimeNanos = JavaMethod("()J")
        getFrameTimelines = JavaMethod("()[Landroid/view/Choreographer$FrameTimeline;")
        getPreferredFrameTimeline = JavaMethod("()Landroid/view/Choreographer$FrameTimeline;")

    class FrameTimeline(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/Choreographer/FrameTimeline"
        getVsyncId = JavaMethod("()J")
        getExpectedPresentationTimeNanos = JavaMethod("()J")
        getDeadlineNanos = JavaMethod("()J")

    class VsyncCallback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/Choreographer/VsyncCallback"
        onVsync = JavaMethod("(Landroid/view/Choreographer$FrameData;)V")