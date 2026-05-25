from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzccr"]

class zzccr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzccr"
    __javaconstructor__ = [("()V", False)]
    zzdd = JavaMethod("(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z")