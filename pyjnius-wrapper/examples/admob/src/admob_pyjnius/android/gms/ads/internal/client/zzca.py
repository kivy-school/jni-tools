from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzca"]

class zzca(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzca"
    __javaconstructor__ = [("()V", False)]
    zzdd = JavaMethod("(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z")