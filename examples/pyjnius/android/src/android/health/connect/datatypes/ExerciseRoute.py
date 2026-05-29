from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExerciseRoute"]

class ExerciseRoute(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/ExerciseRoute"
    __javaconstructor__ = [("(Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getRouteLocations = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Location(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseRoute/Location"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getTime = JavaMethod("()Ljava/time/Instant;")
        getLongitude = JavaMethod("()D")
        getLatitude = JavaMethod("()D")
        getHorizontalAccuracy = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")
        getVerticalAccuracy = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")
        getAltitude = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/health/connect/datatypes/ExerciseRoute/Location/Builder"
            __javaconstructor__ = [("(Ljava/time/Instant;DD)V", False)]
            setHorizontalAccuracy = JavaMethod("(Landroid/health/connect/datatypes/units/Length;)Landroid/health/connect/datatypes/ExerciseRoute$Location$Builder;")
            setVerticalAccuracy = JavaMethod("(Landroid/health/connect/datatypes/units/Length;)Landroid/health/connect/datatypes/ExerciseRoute$Location$Builder;")
            setAltitude = JavaMethod("(Landroid/health/connect/datatypes/units/Length;)Landroid/health/connect/datatypes/ExerciseRoute$Location$Builder;")
            build = JavaMethod("()Landroid/health/connect/datatypes/ExerciseRoute$Location;")