from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcu"]

class zzcu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzcu"
    __javaconstructor__ = [("()V", False)]
    asInterface = JavaStaticMethod("(Landroid/os/IBinder;)Lcom/google/android/gms/ads/internal/client/zzcv;")
    zzdd = JavaMethod("(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z")