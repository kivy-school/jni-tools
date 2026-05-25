from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObserverSpec"]

class ObserverSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/observer/ObserverSpec"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getFilterSchemas = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/observer/ObserverSpec/Builder"
        __javaconstructor__ = [("()V", False)]
        addFilterSchemas = JavaMultipleMethod([("([Ljava/lang/String;)Landroid/app/appsearch/observer/ObserverSpec$Builder;", False, True), ("(Ljava/util/Collection;)Landroid/app/appsearch/observer/ObserverSpec$Builder;", False, False)])
        build = JavaMethod("()Landroid/app/appsearch/observer/ObserverSpec;")