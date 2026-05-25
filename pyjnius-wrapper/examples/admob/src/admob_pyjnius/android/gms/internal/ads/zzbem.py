from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbem"]

class zzbem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbem"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    asBinder = JavaMethod("()Landroid/os/IBinder;")
    onTransact = JavaMethod("(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z")
    zzdd = JavaMethod("(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z")