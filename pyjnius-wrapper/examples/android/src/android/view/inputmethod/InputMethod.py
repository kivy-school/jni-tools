from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputMethod"]

class InputMethod(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InputMethod"
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    SHOW_EXPLICIT = JavaStaticField("I")
    SHOW_FORCED = JavaStaticField("I")
    attachToken = JavaMethod("(Landroid/os/IBinder;)V")
    bindInput = JavaMethod("(Landroid/view/inputmethod/InputBinding;)V")
    unbindInput = JavaMethod("()V")
    startInput = JavaMethod("(Landroid/view/inputmethod/InputConnection;Landroid/view/inputmethod/EditorInfo;)V")
    restartInput = JavaMethod("(Landroid/view/inputmethod/InputConnection;Landroid/view/inputmethod/EditorInfo;)V")
    createSession = JavaMethod("(Landroid/view/inputmethod/InputMethod$SessionCallback;)V")
    setSessionEnabled = JavaMethod("(Landroid/view/inputmethod/InputMethodSession;Z)V")
    revokeSession = JavaMethod("(Landroid/view/inputmethod/InputMethodSession;)V")
    showSoftInput = JavaMethod("(ILandroid/os/ResultReceiver;)V")
    hideSoftInput = JavaMethod("(ILandroid/os/ResultReceiver;)V")
    changeInputMethodSubtype = JavaMethod("(Landroid/view/inputmethod/InputMethodSubtype;)V")

    class SessionCallback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/InputMethod/SessionCallback"
        sessionCreated = JavaMethod("(Landroid/view/inputmethod/InputMethodSession;)V")