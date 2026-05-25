from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Person"]

class Person(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/Person"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toBuilder = JavaMethod("()Landroid/app/Person$Builder;")
    getUri = JavaMethod("()Ljava/lang/String;")
    getName = JavaMethod("()Ljava/lang/CharSequence;")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getKey = JavaMethod("()Ljava/lang/String;")
    isBot = JavaMethod("()Z")
    isImportant = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/Person/Builder"
        __javaconstructor__ = [("()V", False)]
        setName = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/Person$Builder;")
        setIcon = JavaMethod("(Landroid/graphics/drawable/Icon;)Landroid/app/Person$Builder;")
        setUri = JavaMethod("(Ljava/lang/String;)Landroid/app/Person$Builder;")
        setKey = JavaMethod("(Ljava/lang/String;)Landroid/app/Person$Builder;")
        setImportant = JavaMethod("(Z)Landroid/app/Person$Builder;")
        setBot = JavaMethod("(Z)Landroid/app/Person$Builder;")
        build = JavaMethod("()Landroid/app/Person;")