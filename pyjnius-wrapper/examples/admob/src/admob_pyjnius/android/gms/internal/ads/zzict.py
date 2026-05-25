from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzict"]

class zzict(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzict"
    __javaconstructor__ = [("()V", False)]
    zzaC = JavaMethod("()Lcom/google/android/gms/internal/ads/zzict;")
    zzaD = JavaMethod("(Lcom/google/android/gms/internal/ads/zzidp;)Lcom/google/android/gms/internal/ads/zzict;")
    zzaE = JavaMethod("(Lcom/google/android/gms/internal/ads/zzidp;Lcom/google/android/gms/internal/ads/zzidz;)Lcom/google/android/gms/internal/ads/zzict;")
    zzaF = JavaMethod("(Lcom/google/android/gms/internal/ads/zzidl;)Lcom/google/android/gms/internal/ads/zzict;")
    zzaG = JavaMethod("(Lcom/google/android/gms/internal/ads/zzidl;Lcom/google/android/gms/internal/ads/zzidz;)Lcom/google/android/gms/internal/ads/zzict;")
    zzaH = JavaMethod("([B)Lcom/google/android/gms/internal/ads/zzict;")
    zzaI = JavaMethod("([BII)Lcom/google/android/gms/internal/ads/zzict;")
    zzaJ = JavaMethod("([BLcom/google/android/gms/internal/ads/zzidz;)Lcom/google/android/gms/internal/ads/zzict;")
    zzaK = JavaMethod("([BIILcom/google/android/gms/internal/ads/zzidz;)Lcom/google/android/gms/internal/ads/zzict;")
    zzaL = JavaMethod("(Ljava/io/InputStream;)Lcom/google/android/gms/internal/ads/zzict;")
    zzaM = JavaMethod("(Ljava/io/InputStream;Lcom/google/android/gms/internal/ads/zzidz;)Lcom/google/android/gms/internal/ads/zzict;")
    zzaN = JavaMethod("(Ljava/io/InputStream;Lcom/google/android/gms/internal/ads/zzidz;)Z")
    zzaO = JavaMethod("(Ljava/io/InputStream;)Z")
    zzaP = JavaMethod("(Lcom/google/android/gms/internal/ads/zzifz;)Lcom/google/android/gms/internal/ads/zzict;")
    zzaQ = JavaMethod("(Lcom/google/android/gms/internal/ads/zzicu;)Lcom/google/android/gms/internal/ads/zzict;")
    zzaR = JavaStaticMethod("(Lcom/google/android/gms/internal/ads/zzifz;)Lcom/google/android/gms/internal/ads/zzihc;")
    zzaS = JavaStaticMethod("(Ljava/lang/Iterable;Ljava/util/Collection;)V")
    zzaT = JavaStaticMethod("(Ljava/lang/Iterable;Ljava/util/List;)V")