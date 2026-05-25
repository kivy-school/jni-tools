from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractInputMethodService"]

class AbstractInputMethodService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/inputmethodservice/AbstractInputMethodService"
    __javaconstructor__ = [("()V", False)]
    getKeyDispatcherState = JavaMethod("()Landroid/view/KeyEvent$DispatcherState;")
    onCreateInputMethodInterface = JavaMethod("()Landroid/inputmethodservice/AbstractInputMethodService$AbstractInputMethodImpl;")
    onCreateInputMethodSessionInterface = JavaMethod("()Landroid/inputmethodservice/AbstractInputMethodService$AbstractInputMethodSessionImpl;")
    dump = JavaMethod("(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onTrackballEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onGenericMotionEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    getSystemService = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    onDestroy = JavaMethod("()V")
    unregisterComponentCallbacks = JavaMethod("(Landroid/content/ComponentCallbacks;)V")
    onTrimMemory = JavaMethod("(I)V")
    onConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    onLowMemory = JavaMethod("()V")
    registerComponentCallbacks = JavaMethod("(Landroid/content/ComponentCallbacks;)V")

    class AbstractInputMethodImpl(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/inputmethodservice/AbstractInputMethodService/AbstractInputMethodImpl"
        __javaconstructor__ = [("(Landroid/inputmethodservice/AbstractInputMethodService;)V", False)]
        createSession = JavaMethod("(Landroid/view/inputmethod/InputMethod$SessionCallback;)V")
        setSessionEnabled = JavaMethod("(Landroid/view/inputmethod/InputMethodSession;Z)V")
        revokeSession = JavaMethod("(Landroid/view/inputmethod/InputMethodSession;)V")

    class AbstractInputMethodSessionImpl(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/inputmethodservice/AbstractInputMethodService/AbstractInputMethodSessionImpl"
        __javaconstructor__ = [("(Landroid/inputmethodservice/AbstractInputMethodService;)V", False)]
        isEnabled = JavaMethod("()Z")
        isRevoked = JavaMethod("()Z")
        setEnabled = JavaMethod("(Z)V")
        revokeSelf = JavaMethod("()V")
        dispatchKeyEvent = JavaMethod("(ILandroid/view/KeyEvent;Landroid/view/inputmethod/InputMethodSession$EventCallback;)V")
        dispatchTrackballEvent = JavaMethod("(ILandroid/view/MotionEvent;Landroid/view/inputmethod/InputMethodSession$EventCallback;)V")
        dispatchGenericMotionEvent = JavaMethod("(ILandroid/view/MotionEvent;Landroid/view/inputmethod/InputMethodSession$EventCallback;)V")