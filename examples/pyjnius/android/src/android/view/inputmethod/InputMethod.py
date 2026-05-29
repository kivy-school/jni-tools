from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputMethod"]

class InputMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InputMethod"
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    SHOW_EXPLICIT = JavaStaticField("I")
    SHOW_FORCED = JavaStaticField("I")
    bindInput = JavaMethod("(Landroid/view/inputmethod/InputBinding;)V")
    hideSoftInput = JavaMethod("(ILandroid/os/ResultReceiver;)V")
    attachToken = JavaMethod("(Landroid/os/IBinder;)V")
    revokeSession = JavaMethod("(Landroid/view/inputmethod/InputMethodSession;)V")
    changeInputMethodSubtype = JavaMethod("(Landroid/view/inputmethod/InputMethodSubtype;)V")
    setSessionEnabled = JavaMethod("(Landroid/view/inputmethod/InputMethodSession;Z)V")
    startInput = JavaMethod("(Landroid/view/inputmethod/InputConnection;Landroid/view/inputmethod/EditorInfo;)V")
    unbindInput = JavaMethod("()V")
    restartInput = JavaMethod("(Landroid/view/inputmethod/InputConnection;Landroid/view/inputmethod/EditorInfo;)V")
    showSoftInput = JavaMethod("(ILandroid/os/ResultReceiver;)V")
    createSession = JavaMethod("(Landroid/view/inputmethod/InputMethod$SessionCallback;)V")

    class SessionCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/InputMethod$SessionCallback"
        sessionCreated = JavaMethod("(Landroid/view/inputmethod/InputMethodSession;)V")