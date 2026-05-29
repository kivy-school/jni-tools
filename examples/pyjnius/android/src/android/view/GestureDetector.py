from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GestureDetector"]

class GestureDetector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/GestureDetector"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/view/GestureDetector$OnGestureListener;Landroid/os/Handler;)V", False), ("(Landroid/content/Context;Landroid/view/GestureDetector$OnGestureListener;Landroid/os/Handler;Z)V", False), ("(Landroid/content/Context;Landroid/view/GestureDetector$OnGestureListener;)V", False), ("(Landroid/view/GestureDetector$OnGestureListener;Landroid/os/Handler;)V", False), ("(Landroid/view/GestureDetector$OnGestureListener;)V", False)]
    isLongpressEnabled = JavaMethod("()Z")
    setContextClickListener = JavaMethod("(Landroid/view/GestureDetector$OnContextClickListener;)V")
    setIsLongpressEnabled = JavaMethod("(Z)V")
    setOnDoubleTapListener = JavaMethod("(Landroid/view/GestureDetector$OnDoubleTapListener;)V")
    onGenericMotionEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")

    class SimpleOnGestureListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/GestureDetector$SimpleOnGestureListener"
        __javaconstructor__ = [("()V", False)]
        onDoubleTapEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onContextClick = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onDoubleTap = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onSingleTapConfirmed = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onLongPress = JavaMethod("(Landroid/view/MotionEvent;)V")
        onShowPress = JavaMethod("(Landroid/view/MotionEvent;)V")
        onFling = JavaMethod("(Landroid/view/MotionEvent;Landroid/view/MotionEvent;FF)Z")
        onScroll = JavaMethod("(Landroid/view/MotionEvent;Landroid/view/MotionEvent;FF)Z")
        onSingleTapUp = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onDown = JavaMethod("(Landroid/view/MotionEvent;)Z")

    class OnGestureListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/GestureDetector$OnGestureListener"
        onLongPress = JavaMethod("(Landroid/view/MotionEvent;)V")
        onShowPress = JavaMethod("(Landroid/view/MotionEvent;)V")
        onFling = JavaMethod("(Landroid/view/MotionEvent;Landroid/view/MotionEvent;FF)Z")
        onScroll = JavaMethod("(Landroid/view/MotionEvent;Landroid/view/MotionEvent;FF)Z")
        onSingleTapUp = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onDown = JavaMethod("(Landroid/view/MotionEvent;)Z")

    class OnDoubleTapListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/GestureDetector$OnDoubleTapListener"
        onDoubleTapEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onDoubleTap = JavaMethod("(Landroid/view/MotionEvent;)Z")
        onSingleTapConfirmed = JavaMethod("(Landroid/view/MotionEvent;)Z")

    class OnContextClickListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/GestureDetector$OnContextClickListener"
        onContextClick = JavaMethod("(Landroid/view/MotionEvent;)Z")