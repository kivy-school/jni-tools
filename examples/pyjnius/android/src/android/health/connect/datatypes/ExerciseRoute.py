from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExerciseRoute"]

class ExerciseRoute(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/ExerciseRoute"
    __javaconstructor__ = [("(Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getRouteLocations = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Location(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseRoute$Location"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getAltitude = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")
        getLatitude = JavaMethod("()D")
        getLongitude = JavaMethod("()D")
        getHorizontalAccuracy = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")
        getVerticalAccuracy = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getTime = JavaMethod("()Ljava/time/Instant;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/health/connect/datatypes/ExerciseRoute$Location$Builder"
            __javaconstructor__ = [("(Ljava/time/Instant;DD)V", False)]
            setAltitude = JavaMethod("(Landroid/health/connect/datatypes/units/Length;)Landroid/health/connect/datatypes/ExerciseRoute$Location$Builder;")
            setVerticalAccuracy = JavaMethod("(Landroid/health/connect/datatypes/units/Length;)Landroid/health/connect/datatypes/ExerciseRoute$Location$Builder;")
            setHorizontalAccuracy = JavaMethod("(Landroid/health/connect/datatypes/units/Length;)Landroid/health/connect/datatypes/ExerciseRoute$Location$Builder;")
            build = JavaMethod("()Landroid/health/connect/datatypes/ExerciseRoute$Location;")