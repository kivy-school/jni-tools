from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObserverSpec"]

class ObserverSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/observer/ObserverSpec"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getFilterSchemas = JavaMethod("()Ljava/util/Set;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/observer/ObserverSpec$Builder"
        __javaconstructor__ = [("()V", False)]
        addFilterSchemas = JavaMultipleMethod([("(Ljava/util/Collection;)Landroid/app/appsearch/observer/ObserverSpec$Builder;", False, False), ("([Ljava/lang/String;)Landroid/app/appsearch/observer/ObserverSpec$Builder;", False, True)])
        build = JavaMethod("()Landroid/app/appsearch/observer/ObserverSpec;")