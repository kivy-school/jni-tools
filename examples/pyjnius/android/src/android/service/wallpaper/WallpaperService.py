from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WallpaperService"]

class WallpaperService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/wallpaper/WallpaperService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    onCreate = JavaMethod("()V")
    onDestroy = JavaMethod("()V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onCreateEngine = JavaMethod("()Landroid/service/wallpaper/WallpaperService$Engine;")
    dump = JavaMethod("(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")

    class Engine(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/wallpaper/WallpaperService/Engine"
        __javaconstructor__ = [("(Landroid/service/wallpaper/WallpaperService;)V", False)]
        getSurfaceHolder = JavaMethod("()Landroid/view/SurfaceHolder;")
        getWallpaperFlags = JavaMethod("()I")
        getDesiredMinimumWidth = JavaMethod("()I")
        getDesiredMinimumHeight = JavaMethod("()I")
        isVisible = JavaMethod("()Z")
        isPreview = JavaMethod("()Z")
        setTouchEventsEnabled = JavaMethod("(Z)V")
        setOffsetNotificationsEnabled = JavaMethod("(Z)V")
        onCreate = JavaMethod("(Landroid/view/SurfaceHolder;)V")
        onDestroy = JavaMethod("()V")
        onVisibilityChanged = JavaMethod("(Z)V")
        onApplyWindowInsets = JavaMethod("(Landroid/view/WindowInsets;)V")
        onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)V")
        onOffsetsChanged = JavaMethod("(FFFFII)V")
        onCommand = JavaMethod("(Ljava/lang/String;IIILandroid/os/Bundle;Z)Landroid/os/Bundle;")
        onDesiredSizeChanged = JavaMethod("(II)V")
        onSurfaceChanged = JavaMethod("(Landroid/view/SurfaceHolder;III)V")
        onSurfaceRedrawNeeded = JavaMethod("(Landroid/view/SurfaceHolder;)V")
        onSurfaceCreated = JavaMethod("(Landroid/view/SurfaceHolder;)V")
        onSurfaceDestroyed = JavaMethod("(Landroid/view/SurfaceHolder;)V")
        onWallpaperFlagsChanged = JavaMethod("(I)V")
        onZoomChanged = JavaMethod("(F)V")
        notifyColorsChanged = JavaMethod("()V")
        onComputeColors = JavaMethod("()Landroid/app/WallpaperColors;")
        dump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
        getDisplayContext = JavaMethod("()Landroid/content/Context;")