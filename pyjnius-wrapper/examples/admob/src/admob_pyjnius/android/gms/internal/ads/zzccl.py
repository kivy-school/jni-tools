from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzccl"]

class zzccl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzccl"
    __javaconstructor__ = [("()V", False)]
    zzb = JavaStaticMethod("(Landroid/os/IBinder;)Lcom/google/android/gms/internal/ads/zzccm;")
    zzdd = JavaMethod("(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z")