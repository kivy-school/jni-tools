from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzck"]

class zzck(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzck"
    __javaconstructor__ = [("()V", False)]
    zzd = JavaStaticMethod("(Landroid/os/IBinder;)Lcom/google/android/gms/ads/internal/client/zzcl;")
    zzdd = JavaMethod("(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z")