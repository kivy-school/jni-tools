from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GestureDetector"]

class GestureDetector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/GestureDetector"
    __javaconstructor__ = [("(Landroid/view/GestureDetector$OnGestureListener;Landroid/os/Handler;)V", False), ("(Landroid/view/GestureDetector$OnGestureListener;)V", False), ("(Landroid/content/Context;Landroid/view/GestureDetector$OnGestureListener;)V", False), ("(Landroid/content/Context;Landroid/view/GestureDetector$OnGestureListener;Landroid/os/Handler;)V", False), ("(Landroid/content/Context;Landroid/view/GestureDetector$OnGestureListener;Landroid/os/Handler;Z)V", False)]
    setOnDoubleTapListener = JavaMethod("(Landroid/view/GestureDetector$OnDoubleTapListener;)V")
    setContextClickListener = JavaMethod("(Landroid/view/GestureDetector$OnContextClickListener;)V")
    setIsLongpressEnabled = JavaMethod("(Z)V")
    isLongpressEnabled = JavaMethod("()Z")
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onGenericMotionEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")

    class OnContextClickListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/GestureDetector/OnContextClickListener"
        onContextClick = JavaMethod("(Landroid/view/MotionEvent;)Z")

    class OnDoubleTapListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/GestureDetector/OnDoubleTapListener"
        onSingleTapConfirmed = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onDoubleTap = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onDoubleTapEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")

    class OnGestureListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/GestureDetector/OnGestureListener"
        onDown = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onShowPress = JavaMethod("(Landroid/view/MotionEvent;)V")
        onSingleTapUp = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onScroll = JavaMethod("(Landroid/view/MotionEvent;Landroid/view/MotionEvent;FF)Z")
        onLongPress = JavaMethod("(Landroid/view/MotionEvent;)V")
        onFling = JavaMethod("(Landroid/view/MotionEvent;Landroid/view/MotionEvent;FF)Z")

    class SimpleOnGestureListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/GestureDetector/SimpleOnGestureListener"
        __javaconstructor__ = [("()V", False)]
        onSingleTapUp = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onLongPress = JavaMethod("(Landroid/view/MotionEvent;)V")
        onScroll = JavaMethod("(Landroid/view/MotionEvent;Landroid/view/MotionEvent;FF)Z")
        onFling = JavaMethod("(Landroid/view/MotionEvent;Landroid/view/MotionEvent;FF)Z")
        onShowPress = JavaMethod("(Landroid/view/MotionEvent;)V")
        onDown = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onDoubleTap = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onDoubleTapEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onSingleTapConfirmed = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onContextClick = JavaMethod("(Landroid/view/MotionEvent;)Z")