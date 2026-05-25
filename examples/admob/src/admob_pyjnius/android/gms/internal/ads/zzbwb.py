from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbwb"]

class zzbwb(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbwb"
    __javaconstructor__ = [("(Ljava/util/Date;ILjava/util/Set;Landroid/location/Location;ZIZILjava/lang/String;)V", False)]
    getBirthday = JavaMethod("()Ljava/util/Date;")
    getGender = JavaMethod("()I")
    getKeywords = JavaMethod("()Ljava/util/Set;")
    getLocation = JavaMethod("()Landroid/location/Location;")
    isTesting = JavaMethod("()Z")
    taggedForChildDirectedTreatment = JavaMethod("()I")
    isDesignedForFamilies = JavaMethod("()Z")