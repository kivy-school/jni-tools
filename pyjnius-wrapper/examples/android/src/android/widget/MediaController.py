from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaController"]

class MediaController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/MediaController"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Z)V", False), ("(Landroid/content/Context;)V", False)]
    onFinishInflate = JavaMethod("()V")
    setMediaPlayer = JavaMethod("(Landroid/widget/MediaController$MediaPlayerControl;)V")
    setAnchorView = JavaMethod("(Landroid/view/View;)V")
    show = JavaMultipleMethod([("()V", False, False), ("(I)V", False, False)])
    isShowing = JavaMethod("()Z")
    hide = JavaMethod("()V")
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onTrackballEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    dispatchKeyEvent = JavaMethod("(Landroid/view/KeyEvent;)Z")
    setEnabled = JavaMethod("(Z)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    setPrevNextListeners = JavaMethod("(Landroid/view/View$OnClickListener;Landroid/view/View$OnClickListener;)V")

    class MediaPlayerControl(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/MediaController/MediaPlayerControl"
        start = JavaMethod("()V")
        pause = JavaMethod("()V")
        getDuration = JavaMethod("()I")
        getCurrentPosition = JavaMethod("()I")
        seekTo = JavaMethod("(I)V")
        isPlaying = JavaMethod("()Z")
        getBufferPercentage = JavaMethod("()I")
        canPause = JavaMethod("()Z")
        canSeekBackward = JavaMethod("()Z")
        canSeekForward = JavaMethod("()Z")
        getAudioSessionId = JavaMethod("()I")