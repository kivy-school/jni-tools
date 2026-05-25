from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VolumeShaper"]

class VolumeShaper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/VolumeShaper"
    apply = JavaMethod("(Landroid/media/VolumeShaper$Operation;)V")
    replace = JavaMethod("(Landroid/media/VolumeShaper$Configuration;Landroid/media/VolumeShaper$Operation;Z)V")
    getVolume = JavaMethod("()F")
    close = JavaMethod("()V")
    finalize = JavaMethod("()V")

    class Configuration(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/VolumeShaper/Configuration"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CUBIC_RAMP = JavaStaticField("Landroid/media/VolumeShaper$Configuration;")
        INTERPOLATOR_TYPE_CUBIC = JavaStaticField("I")
        INTERPOLATOR_TYPE_CUBIC_MONOTONIC = JavaStaticField("I")
        INTERPOLATOR_TYPE_LINEAR = JavaStaticField("I")
        INTERPOLATOR_TYPE_STEP = JavaStaticField("I")
        LINEAR_RAMP = JavaStaticField("Landroid/media/VolumeShaper$Configuration;")
        SCURVE_RAMP = JavaStaticField("Landroid/media/VolumeShaper$Configuration;")
        SINE_RAMP = JavaStaticField("Landroid/media/VolumeShaper$Configuration;")
        getMaximumCurvePoints = JavaStaticMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        getInterpolatorType = JavaMethod("()I")
        getDuration = JavaMethod("()J")
        getTimes = JavaMethod("()[F")
        getVolumes = JavaMethod("()[F")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/media/VolumeShaper/Configuration/Builder"
            __javaconstructor__ = [("()V", False), ("(Landroid/media/VolumeShaper$Configuration;)V", False)]
            setInterpolatorType = JavaMethod("(I)Landroid/media/VolumeShaper$Configuration$Builder;")
            setDuration = JavaMethod("(J)Landroid/media/VolumeShaper$Configuration$Builder;")
            setCurve = JavaMethod("([F[F)Landroid/media/VolumeShaper$Configuration$Builder;")
            reflectTimes = JavaMethod("()Landroid/media/VolumeShaper$Configuration$Builder;")
            invertVolumes = JavaMethod("()Landroid/media/VolumeShaper$Configuration$Builder;")
            scaleToEndVolume = JavaMethod("(F)Landroid/media/VolumeShaper$Configuration$Builder;")
            scaleToStartVolume = JavaMethod("(F)Landroid/media/VolumeShaper$Configuration$Builder;")
            build = JavaMethod("()Landroid/media/VolumeShaper$Configuration;")

    class Operation(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/VolumeShaper/Operation"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        PLAY = JavaStaticField("Landroid/media/VolumeShaper$Operation;")
        REVERSE = JavaStaticField("Landroid/media/VolumeShaper$Operation;")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")