from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Choreographer"]

class Choreographer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/Choreographer"
    postVsyncCallback = JavaMethod("(Landroid/view/Choreographer$VsyncCallback;)V")
    postFrameCallbackDelayed = JavaMethod("(Landroid/view/Choreographer$FrameCallback;J)V")
    removeFrameCallback = JavaMethod("(Landroid/view/Choreographer$FrameCallback;)V")
    postFrameCallback = JavaMethod("(Landroid/view/Choreographer$FrameCallback;)V")
    removeVsyncCallback = JavaMethod("(Landroid/view/Choreographer$VsyncCallback;)V")
    getInstance = JavaStaticMethod("()Landroid/view/Choreographer;")

    class VsyncCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/Choreographer$VsyncCallback"
        onVsync = JavaMethod("(Landroid/view/Choreographer$FrameData;)V")

    class FrameTimeline(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/Choreographer$FrameTimeline"
        getDeadlineNanos = JavaMethod("()J")
        getExpectedPresentationTimeNanos = JavaMethod("()J")
        getVsyncId = JavaMethod("()J")

    class FrameData(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/Choreographer$FrameData"
        getFrameTimeNanos = JavaMethod("()J")
        getFrameTimelines = JavaMethod("()[Landroid/view/Choreographer$FrameTimeline;")
        getPreferredFrameTimeline = JavaMethod("()Landroid/view/Choreographer$FrameTimeline;")

    class FrameCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/Choreographer$FrameCallback"
        doFrame = JavaMethod("(J)V")