from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgax"]

class zzgax(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgax"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/Looper;)V", False)]
    dispatchMessage = JavaMethod("(Landroid/os/Message;)V")
    zza = JavaMethod("(Landroid/os/Message;)V")