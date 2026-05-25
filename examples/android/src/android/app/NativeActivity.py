from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NativeActivity"]

class NativeActivity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/NativeActivity"
    __javaconstructor__ = [("()V", False)]
    META_DATA_FUNC_NAME = JavaStaticField("Ljava/lang/String;")
    META_DATA_LIB_NAME = JavaStaticField("Ljava/lang/String;")
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    onDestroy = JavaMethod("()V")
    onPause = JavaMethod("()V")
    onResume = JavaMethod("()V")
    onSaveInstanceState = JavaMethod("(Landroid/os/Bundle;)V")
    onStart = JavaMethod("()V")
    onStop = JavaMethod("()V")
    onConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    onLowMemory = JavaMethod("()V")
    onWindowFocusChanged = JavaMethod("(Z)V")
    surfaceCreated = JavaMethod("(Landroid/view/SurfaceHolder;)V")
    surfaceChanged = JavaMethod("(Landroid/view/SurfaceHolder;III)V")
    surfaceRedrawNeeded = JavaMethod("(Landroid/view/SurfaceHolder;)V")
    surfaceDestroyed = JavaMethod("(Landroid/view/SurfaceHolder;)V")
    onInputQueueCreated = JavaMethod("(Landroid/view/InputQueue;)V")
    onInputQueueDestroyed = JavaMethod("(Landroid/view/InputQueue;)V")
    onGlobalLayout = JavaMethod("()V")