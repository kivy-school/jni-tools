from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbel"]

class zzbel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbel"
    __javaconstructor__ = [("(Landroid/os/IBinder;Ljava/lang/String;)V", False)]
    asBinder = JavaMethod("()Landroid/os/IBinder;")
    zza = JavaMethod("()Landroid/os/Parcel;")
    zzcZ = JavaMethod("(ILandroid/os/Parcel;)Landroid/os/Parcel;")
    zzda = JavaMethod("(ILandroid/os/Parcel;)V")
    zzdb = JavaMethod("(ILandroid/os/Parcel;)V")