from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SurfaceSyncGroup"]

class SurfaceSyncGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/SurfaceSyncGroup"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    markSyncReady = JavaMethod("()V")
    addTransaction = JavaMethod("(Landroid/view/SurfaceControl$Transaction;)V")
    add = JavaMultipleMethod([("(Landroid/view/AttachedSurfaceControl;Ljava/lang/Runnable;)Z", False, False), ("(Landroid/view/SurfaceControlViewHost$SurfacePackage;Ljava/lang/Runnable;)Z", False, False)])